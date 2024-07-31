# Task 5 - Event End Time Calculator

def calculate_end_time(hrs, mins, durs):
    total_mins = mins + durs
    new_hrs = (hrs + total_mins // 60) % 24
    new_mins = total_mins % 60

    return new_hrs, new_mins


start_hours = int(input("Enter the starting hour (0-23): "))
start_minutes = int(input("Enter the starting minutes (0-59): "))
duration_minutes = int(input("Enter the duration in minutes: "))

end_hours, end_minutes = calculate_end_time(start_hours, start_minutes, duration_minutes)

print(f"\nEvent will starts at: {start_hours:02}:{start_minutes:02}")
print(f"Event will end at:    {end_hours:02}:{end_minutes:02}")

