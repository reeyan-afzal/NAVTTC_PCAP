class WeekDayError(Exception):
    pass


class Weeker:
    # List of valid days in a week
    __valid_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        # Validate the day input
        if day not in Weeker.__valid_days:
            raise WeekDayError  # Raise exception for invalid day
        self.__day_index = Weeker.__valid_days.index(day)  # Store the index of the current day

    def __str__(self):
        # Return the string representation of the current day
        return Weeker.__valid_days[self.__day_index]

    def add_days(self, n):
        # Move forward n days in the week
        self.__day_index = (self.__day_index + n) % 7  # Use modulus to wrap around

    def subtract_days(self, n):
        # Move backward n days in the week
        self.__day_index = (self.__day_index - n) % 7  # Use modulus to wrap around


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
