import tkinter as tk
from tkinter import ttk, messagebox
import os
import openpyxl
import requests


class DataEntryApp:
    def __init__(self, _root):
        self.accept_var = tk.StringVar(value="Not Accepted")
        self.num_semesters_spinbox = None
        self.num_courses_spinbox = None
        self.reg_status_var = tk.StringVar(value="Not Registered")
        self.nationality_combobox = None
        self.age_spinbox = None
        self.title_combobox = None
        self.last_name_entry = None
        self.first_name_entry = None
        self.root = _root
        self.root.title("Data Entry Form")

        # Frame container
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=10)

        # Call methods to create UI components
        self.create_user_info_section()
        self.create_course_info_section()
        self.create_terms_section()
        self.create_submit_button()

    def create_user_info_section(self):
        user_info_frame = tk.LabelFrame(self.frame, text="User Information")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        # First and Last Name
        tk.Label(user_info_frame, text="First Name").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(user_info_frame)
        self.first_name_entry.grid(row=1, column=0)

        tk.Label(user_info_frame, text="Last Name").grid(row=0, column=1)
        self.last_name_entry = tk.Entry(user_info_frame)
        self.last_name_entry.grid(row=1, column=1)

        # Title
        tk.Label(user_info_frame, text="Title").grid(row=0, column=2)
        self.title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        self.title_combobox.grid(row=1, column=2)

        # Age
        tk.Label(user_info_frame, text="Age").grid(row=2, column=0)
        self.age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
        self.age_spinbox.grid(row=3, column=0)

        # Nationality
        tk.Label(user_info_frame, text="Nationality").grid(row=2, column=1)
        self.nationality_combobox = ttk.Combobox(user_info_frame, values=[
            "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"
        ])
        self.nationality_combobox.grid(row=3, column=1)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_course_info_section(self):
        courses_frame = tk.LabelFrame(self.frame, text="Course Information")
        courses_frame.grid(row=1, column=0, padx=20, pady=10)

        # Registration status
        tk.Label(courses_frame, text="Registration Status").grid(row=0, column=0)
        tk.Checkbutton(
            courses_frame, text="Currently Registered", variable=self.reg_status_var,
            onvalue="Registered", offvalue="Not Registered"
        ).grid(row=1, column=0)

        # Number of courses
        tk.Label(courses_frame, text="# Completed Courses").grid(row=0, column=1)
        self.num_courses_spinbox = tk.Spinbox(courses_frame, from_=0, to=999999)
        self.num_courses_spinbox.grid(row=1, column=1)

        # Number of semesters
        tk.Label(courses_frame, text="# Semesters").grid(row=0, column=2)
        self.num_semesters_spinbox = tk.Spinbox(courses_frame, from_=0, to=999999)
        self.num_semesters_spinbox.grid(row=1, column=2)

        for widget in courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_terms_section(self):
        terms_frame = tk.LabelFrame(self.frame, text="Terms & Conditions")
        terms_frame.grid(row=2, column=0, padx=20, pady=10)

        tk.Checkbutton(
            terms_frame, text="I accept the terms and conditions.", variable=self.accept_var,
            onvalue="Accepted", offvalue="Not Accepted"
        ).grid(row=0, column=0)

    def create_submit_button(self):
        submit_button = tk.Button(self.frame, text="Enter Data", command=self.enter_data, height=2)
        submit_button.grid(row=3, column=0, padx=20, pady=10, sticky="news")

    def enter_data(self):
        """Handler for entering data and saving to an Excel file and Airtable."""
        if self.accept_var.get() == "Accepted":
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()

            if firstname and lastname:
                title = self.title_combobox.get()
                age = self.age_spinbox.get()
                nationality = self.nationality_combobox.get()
                registration_status = self.reg_status_var.get()
                num_courses = self.num_courses_spinbox.get()
                num_semesters = self.num_semesters_spinbox.get()

                print(f"First Name: {firstname}, Last Name: {lastname}")
                print(f"Title: {title}, Age: {age}, Nationality: {nationality}")
                print(f"Courses: {num_courses}, Semesters: {num_semesters}")
                print(f"Registration status: {registration_status}")
                print("------------------------------------------")

                filepath = os.path.join(os.getcwd(), "data.xlsx")

                if not os.path.exists(filepath):
                    workbook = openpyxl.Workbook()
                    sheet = workbook.active
                    heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
                               "Courses", "Semesters", "Registration status"]
                    sheet.append(heading)
                    workbook.save(filepath)

                workbook = openpyxl.load_workbook(filepath)
                sheet = workbook.active
                sheet.append([firstname, lastname, title, age, nationality, num_courses,
                              num_semesters, registration_status])
                workbook.save(filepath)

                # Airtable API details
                api_key = 'SORRY_REMOVING_MY_PERSONAL_ACCESS_TOKEN'
                base_id = 'CONFIDENTIAL'
                table_name = 'CONFIDENTIAL'
                url = f'https://api.airtable.com/v0/{base_id}/{table_name}'

                headers = {
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                }

                data = {
                    "fields": {
                        "First Name": firstname,
                        "Last Name": lastname,
                        "Title": title,
                        "Age": age,
                        "Nationality": nationality,
                        "Courses": num_courses,
                        "Semesters": num_semesters,
                        "Registration status": registration_status
                    }
                }

                response = requests.post(url, headers=headers, json=data)
                # Debugging output
                print(f"Response status code: {response.status_code}")
                print(f"Response content: {response.text}")

                if response.status_code == 201:
                    messagebox.showinfo("Success", "Data saved successfully!")

            else:
                messagebox.showwarning("Error", "First name and last name are required.")
        else:
            messagebox.showwarning("Error", "You have not accepted the terms")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()
