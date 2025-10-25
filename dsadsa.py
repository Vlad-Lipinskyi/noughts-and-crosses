import random

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

for i in board:
    print(i)

currentPlayer = "X"

mode = input("Виберіть режим гри (1 - гравець проти гравця, 2 - проти комп'ютера): ")

for moveNumber in range(0, 9):  
    print("Хід гравця", currentPlayer)

    if mode == "2" and currentPlayer == "O":
        print("Хід комп'ютера...")
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    empty_cells.append((r, c))

        row, col = random.choice(empty_cells)
    else:
        move = input("Введіть рядок і стовпець через пробіл (наприклад: 0 2): ")
        row = int(move[0])
        col = int(move[2])

    if board[row][col] != " ":
        print("Клітина зайнята! Спробуйте ще раз.")
        continue

    board[row][col] = currentPlayer

    for i in board:
        print(i)

    winner = " "

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            winner = board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            winner = board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        winner = board[0][2]

    if winner != " ":
        print("Гравець", winner, "переміг!")
        break

    draw = []

    if board[0][0] != board[1][1] != board[2][2]:
        draw.append("Нічия")
    if board[0][2] != board[1][1] != board[2][0]:
        draw.append("Нічия")

    if board[0][0] != board[0][1] != board[0][2]:
        draw.append("Нічия")
    if board[1][0] != board[1][1] != board[1][2]:
        draw.append("Нічия")
    if board[2][0] != board[2][1] != board[2][2]:
        draw.append("Нічия")

    if board[0][0] != board[1][0] != board[2][0]:
        draw.append("Нічия")
    if board[0][1] != board[1][1] != board[2][1]:
        draw.append("Нічия")
    if board[0][2] != board[1][2] != board[2][2]:
        draw.append("Нічия")

    countDraw = draw.count("Нічия")

    if countDraw == 8:
        empty_found = False

        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    empty_found = True

        if empty_found == False and winner == " ":
            print("Нічия!")
            break
        
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

print("Гру завершено!")
