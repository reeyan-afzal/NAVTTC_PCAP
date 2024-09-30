# Task 72 - Compare Two Dates

from datetime import datetime, date


def check_date_status(given_date):
    today = date.today()

    if given_date < today:
        return "past"
    elif given_date == today:
        return "present"
    else:
        return "future"


d1 = input("Enter the Date 1 (in YYYY-MM-DD format): ")
d2 = input("Enter the Date 2 (in YYYY-MM-DD format): ")

try:
    _d1 = datetime.strptime(d1, "%Y-%m-%d").date()
    _d2 = datetime.strptime(d2, "%Y-%m-%d").date()

    print(f"Date 1 ({_d1}) is in the {check_date_status(_d1)}.")
    print(f"Date 2 ({_d2}) is in the {check_date_status(_d2)}.")
except ValueError:
    print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
