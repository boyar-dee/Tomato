ROWS = 6
COLS = 7

board = []

for i in range(ROWS):
    row = []
    for j in range(COLS):
        row.append("-")
    board.append(row)

current_player = "X"


def print_board():
    for row in board:
        print(*row)
    print("0 1 2 3 4 5 6")


def drop_piece(col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "-":
            board[row][col] = player
            return True

    return False


def check_win(player):

    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True

    return False


running = True

while running:
    print_board()
    print("Player", current_player, "turn")

    col = int(input("Choose a column 0-6: "))

    if col < 0 or col >= COLS:
        print("Invalid column!")
        continue

    success = drop_piece(col, current_player)

    if not success:
        print("That column is full!")
        continue

    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        running = False
    else:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"