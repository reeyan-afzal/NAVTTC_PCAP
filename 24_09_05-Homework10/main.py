"""
Implement a hotel management system, taking an empty list, should show that no rooms is available
Append new rooms using a method, you use room_check_in and room_check_out methods if room is available,
also check the status of room whether empty or reserved by using a method.
"""


from hotel import HotelRoom


if __name__ == "__main__":
    white_lotus = HotelRoom()

    while True:
        print("\n*** Hotel Management System ***")
        print("1. Add a new room")
        print("2. Check into a room")
        print("3. Check out of a room")
        print("4. Check room status")
        print("5. List all rooms")
        print("6. Exit")

        _user_choice = input("\nEnter your choice (1-6): ")

        if _user_choice == "1":
            white_lotus.add_room()

        elif _user_choice == "2":
            room_number = int(input("Enter room number to check in: "))
            white_lotus.room_check_in(room_number)

        elif _user_choice == "3":
            room_number = int(input("Enter room number to check out: "))
            white_lotus.room_check_out(room_number)

        elif _user_choice == "4":
            room_number = int(input("Enter room number to check status: "))
            white_lotus.check_room_status(room_number)

        elif _user_choice == "5":
            white_lotus.list_rooms()

        elif _user_choice == "6":
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
