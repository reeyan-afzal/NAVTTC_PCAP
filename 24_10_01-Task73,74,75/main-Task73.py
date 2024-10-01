# Task 73 - Calender Module

import calendar


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


my_cal = MyCalendar()

print(my_cal.count_weekday_in_year(2019, 0))

print(my_cal.count_weekday_in_year(2000, 6))
