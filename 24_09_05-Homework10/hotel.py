class HotelRoom:
    def __init__(self):
        self._all_rooms = []

    def add_room(self):
        """Adds a new room. Initially, the room is marked as 'False' (available)."""
        self._all_rooms.append(False)
        print(f"Room {len(self._all_rooms)} added. Current status: Available")

    def room_check_in(self, room_number):
        """Check-in to a specific room if available."""
        if 0 < room_number <= len(self._all_rooms):
            if self._all_rooms[room_number - 1]:
                print(f"\nRoom {room_number} is currently occupied!")
            else:
                print(f"\nRoom {room_number} is available. Checking in...")
                self._all_rooms[room_number - 1] = True
        else:
            print("\nNo such room exists. Please enter a valid room number.")

    def room_check_out(self, room_number):
        """Check-out from a specific room if it's currently occupied."""
        if 0 < room_number <= len(self._all_rooms):
            if self._all_rooms[room_number - 1]:
                print(f"\nChecking out from room {room_number}!")
                self._all_rooms[room_number - 1] = False
            else:
                print(f"\nRoom {room_number} is already empty.")
        else:
            print("\nNo such room exists. Please enter a valid room number.")

    def check_room_status(self, room_number):
        """Check the status of a specific room, whether it's available or reserved."""
        if 0 < room_number <= len(self._all_rooms):
            status = "Occupied" if self._all_rooms[room_number - 1] else "Available"
            print(f"\nRoom {room_number} is currently {status}.")
        else:
            print("\nNo such room exists.")

    def list_rooms(self):
        """List all rooms with their status (Occupied or Available)."""
        if not self._all_rooms:
            print("\nNo rooms available.")
            return

        print("\nRoom List:")
        for i, room_status in enumerate(self._all_rooms, start=1):
            status = "Occupied" if room_status else "Available"
            print(f"Room {i}: {status}")
