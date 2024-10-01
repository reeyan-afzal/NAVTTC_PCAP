# Task 75 - Custom MyCalendar 02

import calendar
from datetime import date


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            month_calendar = self.monthdays2calendar(year, month)
            for week in month_calendar:
                for day, week_day in week:
                    if day != 0 and week_day == weekday:
                        count += 1
        return count

    def count_specific_date_in_range(self, day, month, start_year, end_year, weekday):
        count = 0
        for year in range(start_year, end_year + 1):
            try:
                specific_date = date(year, month, day)
                if specific_date.weekday() == weekday:
                    count += 1
            except ValueError:
                continue
        return count

    def find_first_and_last_weekday_in_month(self, year, month, weekday):
        first_occurrence = None
        last_occurrence = None
        month_calendar = self.monthdays2calendar(year, month)

        for week in month_calendar:
            for day, week_day in week:
                if day != 0 and week_day == weekday:
                    if first_occurrence is None:
                        first_occurrence = day
                    last_occurrence = day

        return first_occurrence, last_occurrence


my_cal = MyCalendar()

# Test case
year = 2022
month = 9
weekday = 2

first_last = my_cal.find_first_and_last_weekday_in_month(year, month, weekday)
print(first_last)
