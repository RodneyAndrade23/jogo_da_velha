import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style


def make_move(row, col):
    global current_player

    if game[row][col] == '':
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player)
        check_winner()
        current_player = 'O' if current_player == 'X' else 'X'


def check_winner():

    winning_combinations = (game[0], game[1], game[2],
                            [game[i][0] for i in range(3)],
                            [game[i][1] for i in range(3)],
                            [game[i][2] for i in range(3)],
                            [game[i][i] for i in range(3)],
                            [game[i][2 - i] for i in range(3)])

    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] != '':
            announce_winner(combination[0])

    if all(game[i][j] != '' for i in range(3) for j in range(3)):
        announce_winner('Empate')


def announce_winner(player):
    if player == 'Empate':
        message = 'Jogo empatado!'
    else:
        message = f'Jogador {player} venceu!'
    messagebox.showinfo("Game Over", message)
    reset_game()


def reset_game():
    global game, current_player
    game = [['', '', ''] for _ in range(3)]
    current_player = 'X'
    for row in buttons:
        for button in row:
            button.configure(text='')



root = tk.Tk()
root.title('Jogo da Velha')
style = Style(theme='flatly')


buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = ttk.Button(root, text='', width=11,
                            command=lambda i=i, j=j: make_move(i, j))
        button.grid(row=i, column=j, padx=11, pady=11)
        row.append(button)
    buttons.append(row)


game = [['', '', ''] for _ in range(3)]
current_player = 'X'

root.mainloop()