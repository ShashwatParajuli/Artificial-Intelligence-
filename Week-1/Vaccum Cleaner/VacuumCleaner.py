print("===== VACUUM CLEANER AGENT =====")

roomA = int(input("\nEnter status of Room A:\n1 = Dirty, 0 = Clean: "))
roomB = int(input("\nEnter status of Room B:\n1 = Dirty, 0 = Clean: "))
position = int(input("\nEnter vacuum cleaner position:\n1 = Room A, 2 = Room B: "))

print("\n--- Agent Actions ---")

if position == 1:
    # Vacuum is in Room A

    if roomA == 1:
        print("Room A is dirty.")
        print("Action: SUCK")
        roomA = 0
    else:
        print("Room A is already clean.")

    print("Action: MOVE RIGHT to Room B")
    position = 2

    if roomB == 1:
        print("Room B is dirty.")
        print("Action: SUCK")
        roomB = 0
    else:
        print("Room B is already clean.")

elif position == 2:
    # Vacuum is in Room B

    if roomB == 1:
        print("Room B is dirty.")
        print("Action: SUCK")
        roomB = 0
    else:
        print("Room B is already clean.")

    print("Action: MOVE LEFT to Room A")
    position = 1

    if roomA == 1:
        print("Room A is dirty.")
        print("Action: SUCK")
        roomA = 0
    else:
        print("Room A is already clean.")

else:
    print("Invalid position!")

# Goal test
if roomA == 0 and roomB == 0:
    print("\nGoal achieved!")
    print("Both rooms are clean.")
    print("Name:Shashwat Parajuli")
    print("USN:1BF24CS279")
