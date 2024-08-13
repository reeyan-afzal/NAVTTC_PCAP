from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import QByteArray, QBuffer, QIODevice, Qt
from PyQt6.QtGui import QFont
import os
import random


class CustomMessageBox(QDialog):
    def __init__(self, title, message, retry_callback, parent=None):
        super().__init__(parent)
        self.retry_callback = retry_callback
        self.setWindowTitle(title)

        layout = QVBoxLayout(self)

        message_label = QLabel(message, self)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_label.setTextFormat(Qt.TextFormat.RichText)
        font = QFont()
        font.setPointSize(16)
        message_label.setFont(font)
        layout.addWidget(message_label)

        button_layout = QHBoxLayout()

        retry_button = QPushButton("Retry", self)
        retry_button.clicked.connect(self.retry)
        retry_button.setDefault(True)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(lambda: exit())
        close_button.setDefault(False)

        button_layout.addWidget(close_button)
        button_layout.addWidget(retry_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def retry(self):
        if self.retry_callback:
            self.retry_callback()
        self.close()


class UIFORM(object):
    def __init__(self):
        self.buttons = []
        self._bot_score = 0
        self._user_score = 0
        self.current_player = "X"

        self.icons = {
            "X": QtGui.QIcon(os.path.join(os.getcwd(), "resources", "cross.png")),
            "O": QtGui.QIcon(os.path.join(os.getcwd(), "resources", "circle.png")),
            "trophy": QtGui.QIcon(os.path.join(os.getcwd(), "resources", "trophy.png")),
            "lose": QtGui.QIcon(os.path.join(os.getcwd(), "resources", "lose.png")),
            "draw": QtGui.QIcon(os.path.join(os.getcwd(), "resources", "draw.png"))
        }

    def setup_ui(self, Form):
        Form.setObjectName("Tic Tac Toe - PyQT6")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("main_layout")

        self.tic_tac_buttons_layout = QtWidgets.QGridLayout()
        self.tic_tac_buttons_layout.setObjectName("tic_tac_buttons_layout")
        self.generate_tic_tac_toe_buttons()
        self.verticalLayout.addLayout(self.tic_tac_buttons_layout)

        self.stats_layout = QtWidgets.QHBoxLayout()
        self.stats_layout.setObjectName("stats_layout")
        self.add_stats_widgets()
        self.verticalLayout.addLayout(self.stats_layout)

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add_stats_widgets(self):
        self.times_user_won_label = self.create_label("Times User Won: ")
        self._user_score_label = self.create_label(str(self._user_score))
        self.times_bot_won_label = self.create_label("Times Bot Won: ")
        self._bot_score_label = self.create_label(str(self._bot_score))

        spacer_items = [
            QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum),
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum),
            QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        ]

        for item in spacer_items:
            self.stats_layout.addItem(item)

        self.stats_layout.addWidget(self.times_user_won_label)
        self.stats_layout.addWidget(self._user_score_label)
        self.stats_layout.addWidget(self.times_bot_won_label)
        self.stats_layout.addWidget(self._bot_score_label)

    def create_label(self, text):
        label = QtWidgets.QLabel()
        label.setText(text)
        return label

    def generate_tic_tac_toe_buttons(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QtWidgets.QPushButton()
                button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                                           QtWidgets.QSizePolicy.Policy.Expanding))
                button.setMinimumSize(QtCore.QSize(100, 100))
                button.setIconSize(QtCore.QSize(150, 150))
                button.setObjectName(f"tic_tac_button{row + 1}x{col + 1}")
                button.clicked.connect(lambda _, r=row, c=col: self.on_button_click(r, c))
                self.tic_tac_buttons_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        if self.current_player == "X":
            button.setIcon(self.icons["X"])
            self.current_player = "O"
            button.setEnabled(False)
            if not self.check_winner():
                self.bot_move()

    def bot_move(self):
        available_buttons = [(r, c) for r in range(3) for c in range(3) if self.buttons[r][c].isEnabled()]
        if available_buttons:
            row, col = random.choice(available_buttons)
            button = self.buttons[row][col]
            button.setIcon(self.icons["O"])
            self.current_player = "X"
            button.setEnabled(False)
            self.check_winner()

    def check_winner(self):
        for r in range(3):
            if (self.buttons[r][0].icon().cacheKey() == self.buttons[r][1].icon().cacheKey() == self.buttons[r][
                2].icon().cacheKey()) and not self.buttons[r][0].isEnabled():
                self.end_game(self.buttons[r][0].icon())
                return True
        for c in range(3):
            if (self.buttons[0][c].icon().cacheKey() == self.buttons[1][c].icon().cacheKey() == self.buttons[2][
                c].icon().cacheKey()) and not self.buttons[0][c].isEnabled():
                self.end_game(self.buttons[0][c].icon())
                return True
        if (self.buttons[0][0].icon().cacheKey() == self.buttons[1][1].icon().cacheKey() == self.buttons[2][
            2].icon().cacheKey()) and not self.buttons[0][0].isEnabled():
            self.end_game(self.buttons[0][0].icon())
            return True
        if (self.buttons[0][2].icon().cacheKey() == self.buttons[1][1].icon().cacheKey() == self.buttons[2][
            0].icon().cacheKey()) and not self.buttons[0][2].isEnabled():
            self.end_game(self.buttons[0][2].icon())
            return True
        if all(not button.isEnabled() for row in self.buttons for button in row):
            self.end_game(None)
            return True
        return False

    def end_game(self, winner_icon):
        if winner_icon is None:
            message = "It's a draw!"
            icon = self.icons["draw"]
        elif winner_icon.cacheKey() == self.icons["X"].cacheKey():
            message = "You won!"
            icon = self.icons["trophy"]
            self._user_score += 1
        else:
            message = "Bot won!"
            icon = self.icons["lose"]
            self._bot_score += 1

        detailed_message = self.create_detailed_message(icon, message)

        self._user_score_label.setText(str(self._user_score))
        self._bot_score_label.setText(str(self._bot_score))

        msg_box = CustomMessageBox("Game Result", detailed_message, self.reset_game)
        msg_box.exec()

    def create_detailed_message(self, icon, message):
        pixmap = icon.pixmap(64, 64)
        image = pixmap.toImage()
        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.ReadWrite)
        image.save(buffer, "PNG")
        img_data = QByteArray(buffer.data()).toBase64().data().decode()
        return f"<img src='data:image/png;base64,{img_data}' width='64' height='64'><br>{message}"

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(True)
                button.setIcon(QtGui.QIcon())
        self.current_player = "X"

    def retranslate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tic Tac Toe - PyQT6"))
        self.times_user_won_label.setText(_translate("Form", "Times User Won: "))
        self.times_bot_won_label.setText(_translate("Form", "Times Bot Won: "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WidgetForm = QtWidgets.QWidget()
    ui = UIFORM()
    ui.setup_ui(WidgetForm)
    WidgetForm.show()
    sys.exit(app.exec())
