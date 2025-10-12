board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# print(board)

for i in board: 
    print(i)

playerX = input("x | Введіть свій хід (2 числа через пробіл, 1 число це - рядок, а 2 число розташування в рядку): ")
firstSymbolX = int(playerX[0])
secondSymbolX = int(playerX[2])
board[firstSymbolX][secondSymbolX] = "X"

for i in board: 
    print(i)

playerO = input("o | Введіть свій хід (2 числа через пробіл, 1 число це - рядок, а 2 число розташування в рядку): ")
firstSymbolO = int(playerO[0])
secondSymbolO = int(playerO[2])

if board[firstSymbolO][secondSymbolO] != " ":
    print("Клітина занята! Спробуйте ще раз.")

board[firstSymbolO][secondSymbolO] = "O"

for i in board: 
    print(i)
