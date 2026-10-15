# Vacuum Cleaner World

def vacuum_world():
    # Initial state of the rooms
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    print("Initial State:", rooms)
    print("Vacuum starts in Room", location)

    while 'Dirty' in rooms.values():
        if rooms[location] == 'Dirty':
            print("Room", location, "is Dirty. Cleaning...")
            rooms[location] = 'Clean'
        else:
            print("Room", location, "is already Clean.")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

        print("Current State:", rooms)

    print("All rooms are Clean!")
    print("Final State:", rooms)


vacuum_world()
Sample Output
text
Initial State: {'A': 'Dirty', 'B': 'Dirty'}
Vacuum starts in Room A
Room A is Dirty. Cleaning...
Current State: {'A': 'Clean', 'B': 'Dirty'}
Room B is Dirty. Cleaning...
Current State: {'A': 'Clean', 'B': 'Clean'}
All rooms are Clean!
Final State: {'A': 'Clean', 'B': 'Clean'}
Algorithm
Start the vacuum cleaner in Room A.

Check whether the current room is dirty.

If dirty, clean the room.

Move to the other room.

Repeat until both rooms are clean.

Stop the program.

Concept: Artificial Intelligence — Simple Reflex Agent in a Vacuum Cleaner World.


