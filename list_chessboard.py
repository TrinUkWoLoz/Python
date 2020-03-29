# Maps chessboard places and then maps rooks to places

EMPTY = "-"
ROOK = "ROOK"
board = []

#Mapping board using loop, range, variable and append
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

#Mapping all the rooks using indicies
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

#Print result
print(board)