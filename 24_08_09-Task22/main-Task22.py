# Task 22 - Making a Chess Board

board = []
EMPTY = "-"

B_KING = "♚"
B_QUEEN = "♛"
B_ROOK = "♜"
B_BISHOP = "♝"
B_KNIGHT = "♞"
B_PAWN = "♟"

W_KING = "♔"
W_QUEEN = "♕"
W_ROOK = "♖"
W_BISHOP = "♗"
W_KNIGHT = "♘"
W_PAWN = "♙"

for i in range(8):
    row = [EMPTY for r in range(8)]
    board.append(row)

board[0][0] = B_ROOK
board[0][1] = B_KNIGHT
board[0][2] = B_BISHOP
board[0][3] = B_KING
board[0][4] = B_QUEEN
board[0][5] = B_BISHOP
board[0][6] = B_KNIGHT
board[0][7] = B_ROOK
board[1][0] = B_PAWN
board[1][1] = B_PAWN
board[1][2] = B_PAWN
board[1][3] = B_PAWN
board[1][4] = B_PAWN
board[1][5] = B_PAWN
board[1][6] = B_PAWN
board[1][7] = B_PAWN

board[6][0] = W_PAWN
board[6][1] = W_PAWN
board[6][2] = W_PAWN
board[6][3] = W_PAWN
board[6][4] = W_PAWN
board[6][5] = W_PAWN
board[6][6] = W_PAWN
board[6][7] = W_PAWN
board[7][0] = W_ROOK
board[7][1] = W_KNIGHT
board[7][2] = W_BISHOP
board[7][3] = W_QUEEN
board[7][4] = W_KING
board[7][5] = W_BISHOP
board[7][6] = W_KNIGHT
board[7][7] = W_ROOK

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=" ")
    print()
