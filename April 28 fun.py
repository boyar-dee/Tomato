import tkinter as tk

current_player = "X"
buttons = []

def check_win():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player

    if check_win():
        label.config(text=f"Player {current_player} wins!")
        disable_buttons()
        return

    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state="disabled")

root = tk.Tk()
root.title("Tic Tac Toe")

label = tk.Label(root, text="Player X's turn", font=("Arial", 20))
label.grid(row=0, column=0, columnspan=3)

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(
            root,
            text="",
            font=("Arial", 40),
            width=5,
            height=2,
            command=lambda r=row, c=col: button_click(r, c)
        )
        button.grid(row=row + 1, column=col)
        button_row.append(button)
    buttons.append(button_row)

root.mainloop()