import sys
import os
import re

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QSpinBox,
                             QPushButton, QFileDialog, QMessageBox, QLabel, QCheckBox, QCalendarWidget, QComboBox)
from PyQt6.QtCore import QDate, Qt
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def upload_to_drive(file_path):
    """Upload file to Google Drive and return the shareable URL."""
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = 'credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'mimeType': 'image/jpeg'
    }
    media = MediaFileUpload(file_path, mimetype='image/jpeg')

    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')

    # Make file public
    permission = {
        'type': 'anyone',
        'role': 'reader',
    }
    service.permissions().create(fileId=file_id, body=permission).execute()

    return f'https://drive.google.com/uc?id={file_id}'


def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


def validate_phone(phone):
    return len(re.sub(r'\D', '', phone)) == 11


class DataEntryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.email_entry = None
        self.age_spinbox = None
        self.cnic_entry = None
        self.phone_entry = None
        self.last_name_entry = None
        self.first_name_entry = None
        self.browse_button = None
        self.calendar = None
        self.course_selected_entry = None
        self.photo_path = None
        self.photo_preview_label = None
        self.accept_var = None
        self.date_of_joining = None
        self.existing_cnic_cache = set()
        self.initUI()
        self.load_existing_cnic()

    def initUI(self):
        self.setWindowTitle('Data Entry Form')

        # Set a modern color scheme
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #f0f0f0;
            }
            QPushButton {
                background-color: #f0ad4e;
                border: none;
                padding: 10px;
                color: #2e2e2e;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ec971f;
            }
            QLineEdit, QComboBox, QSpinBox {
                background-color: #3e3e3e;
                border: 1px solid #f0ad4e;
                color: #f0f0f0;
                padding: 5px;
            }
            QCalendarWidget {
                background-color: #3e3e3e;
                color: #f0f0f0;
            }
        """)

        layout = QFormLayout()

        # Photo preview QLabel
        self.photo_preview_label = QLabel("Upload Photo")
        self.photo_preview_label.setStyleSheet("border: 1px solid #f0ad4e;")
        self.photo_preview_label.setFixedSize(150, 150)
        self.photo_preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(QLabel('Photo Preview:'), self.photo_preview_label)

        # Photo
        self.photo_path = QLineEdit()
        self.photo_path.setPlaceholderText('Select a photo file')
        self.browse_button = QPushButton('Browse for Image')
        self.browse_button.clicked.connect(self.browse_file)

        layout.addRow(QLabel('Photo:'), self.photo_path)
        layout.addRow(self.browse_button)


        # First Name
        self.first_name_entry = QLineEdit()
        self.first_name_entry.setMinimumWidth(300)

        # Last Name
        self.last_name_entry = QLineEdit()
        self.last_name_entry.setMinimumWidth(300)

        # CNIC
        self.cnic_entry = QLineEdit()
        self.cnic_entry.setPlaceholderText('Enter your cnic')
        self.cnic_entry.textChanged.connect(self.format_cnic)

        # Age
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setMinimum(18)
        self.age_spinbox.setMaximum(40)

        # Email Address
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText('Enter your email')
        self.email_entry.setMinimumWidth(300)
        self.email_entry.textChanged.connect(self.format_email)

        # Phone Number
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText('Enter 11-digit phone number')
        self.phone_entry.setMaxLength(11)
        self.phone_entry.setMinimumWidth(250)
        self.phone_entry.setText('03')
        self.phone_entry.textChanged.connect(self.format_phone)

        # Course Selection ComboBox
        self.course_selected_entry = QComboBox()
        self.course_selected_entry.addItems([
            "Advanced Python & Applications",
            "Cyber Security Expert",
            "Graphic Designing"
        ])

        # Calendar Widget for Date of Joining
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setSelectedDate(QDate.currentDate())
        self.update_date()
        self.calendar.setFixedSize(250, 200)
        self.calendar.clicked.connect(self.update_date)

        layout.addRow(QLabel('First Name:'), self.first_name_entry)
        layout.addRow(QLabel('Last Name:'), self.last_name_entry)
        layout.addRow(QLabel('CNIC:'), self.cnic_entry)
        layout.addRow(QLabel('Age:'), self.age_spinbox)
        layout.addRow(QLabel('Email Address:'), self.email_entry)
        layout.addRow(QLabel('Phone Number:'), self.phone_entry)
        layout.addRow(QLabel('Course Selected:'), self.course_selected_entry)
        layout.addRow(QLabel('Date Of Joining:'), self.calendar)

        self.accept_var = QCheckBox('I accept the terms and conditions.')
        layout.addRow(self.accept_var)

        submit_button = QPushButton('Enter Data')
        submit_button.clicked.connect(self.enter_data)

        layout.addRow(submit_button)

        self.setLayout(layout)
        self.setGeometry(100, 100, 500, 600)

    def browse_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilters(["Image Files (*.png *.jpg *.jpeg)", "All Files (*)"])
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                self.photo_path.setText(file_paths[0])
                self.display_photo(file_paths[0])

    def display_photo(self, file_path):
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.photo_preview_label.size(),
                                          aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.photo_preview_label.setPixmap(scaled_pixmap)
        else:
            self.photo_preview_label.setText("Invalid Image")

    def update_date(self):
        self.date_of_joining = self.calendar.selectedDate().toString("yyyy-MM-dd")

    def format_cnic(self):
        cnic = re.sub(r'\D', '', self.cnic_entry.text())

        if len(cnic) > 0:
            if len(cnic) > 5:
                cnic = cnic[:5] + '-' + cnic[5:]
            if len(cnic) > 13:
                cnic = cnic[:13] + '-' + cnic[13:]

        if len(cnic) > 15:
            cnic = cnic[:15]

        self.cnic_entry.setText(cnic)
        self.cnic_entry.setCursorPosition(len(cnic))

    def format_email(self):
        email = self.email_entry.text()
        if '@' not in email:
            self.email_entry.setStyleSheet('color: red;')
        else:
            self.email_entry.setStyleSheet('color: green;')

    def format_phone(self):
        current_text = self.phone_entry.text()

        user_input = re.sub(r'\D', '', current_text[2:])  # Skip '03' and remove non-digits

        if len(user_input) > 9:
            user_input = user_input[:9]

        self.phone_entry.setText(f'03{user_input}')
        self.phone_entry.setCursorPosition(len(self.phone_entry.text()))

    def load_existing_cnic(self):
        try:
            scope = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive",
            ]
            creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
            client = gspread.authorize(creds)
            sheet = client.open("NAVTTC-DataEntryApp").sheet1
            existing_cnic = sheet.col_values(4)
            self.existing_cnic_cache = set(existing_cnic)

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to load existing CNICs: {e}')

    def enter_data(self):
        if self.accept_var.isChecked():
            firstname = self.first_name_entry.text().capitalize()
            lastname = self.last_name_entry.text().capitalize()
            cnic = self.cnic_entry.text().replace('-', '')
            age = self.age_spinbox.value()
            email = self.email_entry.text()
            phone = self.phone_entry.text()
            course_selected = self.course_selected_entry.currentText()
            photo = self.photo_path.text()

            if cnic in self.existing_cnic_cache:
                QMessageBox.warning(self, 'Duplicate Entry', 'CNIC already exists. Please enter a different CNIC.')
                return

            if not validate_email(email):
                QMessageBox.warning(self, 'Invalid Email', 'Please enter a valid email address.')
                return

            if not validate_phone(phone):
                QMessageBox.warning(self, 'Invalid Phone Number', 'Please enter a valid phone number with 11 digits.')
                return

            if photo:
                try:
                    photo_url = upload_to_drive(photo)
                except Exception as e:
                    QMessageBox.warning(self, 'Upload Error', f'Failed to upload photo: {e}')
                    return
            else:
                photo_url = 'No photo uploaded'

            try:
                scope = [
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive.file",
                    "https://www.googleapis.com/auth/drive",
                ]
                creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
                client = gspread.authorize(creds)
                sheet = client.open("NAVTTC-DataEntryApp").sheet1
                sheet.append_row(
                    [photo_url, firstname, lastname, cnic, age, email, phone, course_selected, self.date_of_joining])
                self.existing_cnic_cache.add(cnic)
                QMessageBox.information(self, 'Success', 'Data entered successfully!')
                self.clear_form()
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Failed to enter data: {e}')
        else:
            QMessageBox.warning(self, 'Terms not accepted', 'You must accept the terms and conditions to proceed.')

    def clear_form(self):
        self.first_name_entry.clear()
        self.last_name_entry.clear()
        self.cnic_entry.clear()
        self.phone_entry.clear()
        self.email_entry.clear()
        self.age_spinbox.setValue(18)
        self.course_selected_entry.setCurrentIndex(0)
        self.photo_path.clear()
        self.accept_var.setChecked(False)
        self.calendar.setSelectedDate(QDate.currentDate())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataEntryApp()
    ex.show()
    sys.exit(app.exec())
