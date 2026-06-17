board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

current_player = "X"

def print_board():
    for row in board:
        print(*row)

def check_win(player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

running = True

while running:
    print_board()
    print("Player", current_player, "turn")

    row = int(input("Enter row 0, 1, or 2: "))
    col = int(input("Enter column 0, 1, or 2: "))

    if board[row][col] != "-":
        print("That space is already taken. Try again.")
        continue

    board[row][col] = current_player

    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        running = False
        continue

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"