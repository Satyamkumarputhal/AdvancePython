rooms ={
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}

occupied_rooms = set()

while True:
    print("\n1. Allot Room")
    print("2. Vacate Room")
    print("3. Check Room Info")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ") 
        room_number = int(input("Enter room number to allot: "))
        if room_number in rooms:
            if rooms[room_number] is None:
                rooms[room_number] = name
                occupied_rooms.add(room_number)
                print(f"Room {room_number} allotted to {name}.")
            else:
                print(f"Room {room_number} is already occupied by {rooms[room_number]}.")
                print("Available rooms -")
                for room, occupant in rooms.items():
                    if occupant is None:
                        print(f"Room {room} is available.")
                
    elif choice == 2:
        room_number = int(input("Enter room number to vacate: "))
        if room_number in rooms:
            if rooms[room_number] is not None:
                print(f"Room {room_number} vacated by {rooms[room_number]}.")
            rooms[room_number] = None
            occupied_rooms.discard(room_number)
        else:
            print(f"Room {room_number} does not exist.")
    elif choice == 3:
        room_number = int(input("Enter room number to check info: "))
        if room_number in rooms:
            if rooms[room_number] is not None:
                print(f"Room {room_number} is occupied by {rooms[room_number]}.")
            else:
                print(f"Room {room_number} is vacant.")
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")