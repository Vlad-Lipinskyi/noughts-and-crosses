# Створили поле гри
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

for i in board:
        print(i)

# Хід першого гравця
currentPlayer = "X"

# Цикл інпута для запиту куди хоче походити гравець
for moveNumber in range(0, 10):  
    print("Хід гравця", currentPlayer)
    move = input("Введіть рядок і стовпець через пробіл (наприклад: 1 2): ")


# Записали хід гравця
    row = int(move[0])
    col = int(move[2])

# Перевірка чи занята клітинка
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

    for rowDraw in range(3):
        if board[i][0] != board[i][1] != board[i][2]:
            draw.append("Нічия")

    # for j in range(3):
    #     if board[0][j] != board[1][j] != board[2][j]:
    #         draw.append("Нічия")

    if board[0][0] != board[1][1] != board[2][2]:
        draw.append("Нічия")
    if board[0][2] != board[1][1] != board[2][0]:
        draw.append("Нічия")
        
    countDraw = draw.count("Нічия")

    if countDraw == 3:
        print("Нічия!")
    print(countDraw)


    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


print("Гру завершено!")