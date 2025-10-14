board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

currentPlayer = "X"

for moveNumber in range(5, 10):  
    print("Хід гравця", currentPlayer)
    move = input("Введіть рядок і стовпець через пробіл (наприклад: 1 2): ")

    row = int(move[0])
    col = int(move[2])

    if board[row][col] != " ":
        print("Клітина зайнята! Спробуйте ще раз.")
        continue

    board[row][col] = currentPlayer

    for i in board:
        print(i)

    winner = " "