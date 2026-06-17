#turn = 1
#stones = 7
#running = True
#while running:
#   print("#Stones:", stones, "     Player", turn)
#   choice = int(input("Enter your choice: "))
#   if choice == 1:
#       stones -= 1
#   if choice == 2:
#      stones -= 2
#   if stones <= 0:
#       print("Player", turn, "won the game")
#       running = False
#   turn = 3 - turn

turn = 1
stones = 7
running = True
while running:
    print("#Stones:", stones, "Player", turn)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        stones -= 1

        if stones == 0:
            print("Player", turn, "won the game")
            running = False

        else:
            turn = 3 - turn

    elif choice == 2:
        stones -= 2
        if stones == 0:
            print("Player", turn, "won the game")
            running = False
        else:
            turn = 3 - turn

    else:
        print("Invalid choice. Enter 1 or 2.")