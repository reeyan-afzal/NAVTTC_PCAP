# Task 5 - Event End Time Calculator

try:
    while True:
        start_hours = int(input("Enter the starting hour (0-23): "))
        start_minutes = int(input("Enter the starting minutes (0-59): "))
        duration_minutes = int(input("Enter the duration in minutes: "))

        if 0 < start_hours < 23 and 0 < start_minutes < 59:
            break
        else:
            print("\nInvalid Values!\n")

    total_mins = start_minutes + duration_minutes
    new_hrs = (start_hours + total_mins // 60) % 24
    new_mins = total_mins % 60

    print(f"\nEvent will starts at: {start_hours:02}:{start_minutes:02}")
    print(f"Event will end at:    {new_hrs:02}:{new_mins:02}")

except KeyboardInterrupt:
    exit()
