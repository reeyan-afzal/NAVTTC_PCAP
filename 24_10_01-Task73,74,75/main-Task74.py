# Task 74 - Custom MyCalendar

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


my_cal = MyCalendar()

# Test case
_start_year = 2000
_end_year = 2020
_day = 25
_month = 12
_weekday = 0

result = my_cal.count_specific_date_in_range(_day, _month, _start_year, _end_year, _weekday)
print(result)
