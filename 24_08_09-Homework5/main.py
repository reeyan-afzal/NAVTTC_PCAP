from rich.console import Console
from rich.table import Table
import chess
import chess.engine

EMPTY = " "
LABELS = ["A", "B", "C", "D", "E", "F", "G", "H"]

B_PIECES = {
    "K": "♚",
    "Q": "♛",
    "R": "♜",
    "B": "♝",
    "N": "♞",
    "P": "♟"
}

W_PIECES = {
    "K": "♔",
    "Q": "♕",
    "R": "♖",
    "B": "♗",
    "N": "♘",
    "P": "♙"
}

console = Console()


def create_board():
    return [[EMPTY for _ in range(8)] for _ in range(8)]


def setup_pieces(board):
    board[7] = [B_PIECES["R"], B_PIECES["N"], B_PIECES["B"], B_PIECES["Q"], B_PIECES["K"], B_PIECES["B"], B_PIECES["N"],
                B_PIECES["R"]]
    board[6] = [B_PIECES["P"]] * 8
    board[1] = [W_PIECES["P"]] * 8
    board[0] = [W_PIECES["R"], W_PIECES["N"], W_PIECES["B"], W_PIECES["Q"], W_PIECES["K"], W_PIECES["B"], W_PIECES["N"],
                W_PIECES["R"]]
    return board


def print_board(board):
    table = Table(show_header=False, show_edge=False, show_lines=True)

    table.add_column("", width=4, justify="center")
    for _ in range(8):
        table.add_column("", width=4, justify="center")
    table.add_column("", width=4, justify="center")

    top_row = [""] + [f" {label} " for label in LABELS] + [""]
    table.add_row(*top_row)

    for i, row in enumerate(reversed(board), 1):
        row_number = 9 - i
        board_row = [f" {row_number} "] + row + [f" {row_number} "]
        table.add_row(*board_row)

    table.add_row("", *[f" {label} " for label in LABELS] + [""])

    console.clear()
    console.print(table)


def move_piece(board, from_square, to_square):
    from_col = LABELS.index(from_square[0].upper())
    from_row = int(from_square[1]) - 1
    to_col = LABELS.index(to_square[0].upper())
    to_row = int(to_square[1]) - 1

    board[to_row][to_col] = board[from_row][from_col]
    board[from_row][from_col] = EMPTY


def is_valid_move(board, from_square, to_square, chess_board, piece_type):
    from_square_uci = from_square.lower()
    to_square_uci = to_square.lower()
    move = chess.Move.from_uci(from_square_uci + to_square_uci)

    from_col = LABELS.index(from_square[0].upper())
    from_row = int(from_square[1]) - 1
    actual_piece = board[from_row][from_col]

    if actual_piece != piece_type:
        print(f"Invalid piece type at {from_square}. Expected {piece_type}, found {actual_piece}.")
        return False

    return move in chess_board.legal_moves


def player_move(board, chess_board):
    print_board(board)
    piece_name = input("\nEnter the piece to move: ").strip().upper()
    from_square = input("Enter the square to move from: ").upper()
    to_square = input("Enter the square to move to: ").upper()

    piece_map = {"PAWN": "♟", "KNIGHT": "♞", "BISHOP": "♝", "ROOK": "♜", "QUEEN": "♛", "KING": "♚"}
    piece_type = piece_map.get(piece_name, None)

    if piece_type is None:
        print(f"\nInvalid piece name: {piece_name}\n")
        return False

    if is_valid_move(board, from_square, to_square, chess_board, piece_type):
        move_piece(board, from_square, to_square)
        chess_board.push(chess.Move.from_uci(from_square.lower() + to_square.lower()))
        print("\nYour move has been made.\n")
        return True
    else:
        print("\nInvalid move. Please try again.\n")
        return False


def bot_move(board, chess_board, engine):
    result = engine.play(chess_board, chess.engine.Limit(time=2.0))
    chess_board.push(result.move)

    from_square = chess.square_name(result.move.from_square).upper()
    to_square = chess.square_name(result.move.to_square).upper()

    move_piece(board, from_square, to_square)
    print(f"Bot moved from {from_square} to {to_square}.\n")


def main():
    board = create_board()
    board = setup_pieces(board)
    chess_board = chess.Board()

    engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

    bot_move(board, chess_board, engine)

    while not chess_board.is_game_over():
        move_made = False
        while not move_made:
            move_made = player_move(board, chess_board)

        if chess_board.is_checkmate():
            print_board(board)
            console.print("Checkmate! You win!")
            break
        elif chess_board.is_stalemate():
            print_board(board)
            console.print("Stalemate! It's a draw!")
            break
        elif chess_board.is_insufficient_material():
            print_board(board)
            console.print("Draw due to insufficient material!")
            break

        bot_move(board, chess_board, engine)
        if chess_board.is_checkmate():
            print_board(board)
            console.print("Checkmate! The bot wins!")
            break
        elif chess_board.is_stalemate():
            print_board(board)
            console.print("Stalemate! It's a draw!")
            break
        elif chess_board.is_insufficient_material():
            print_board(board)
            console.print("Draw due to insufficient material!")
            break

    print_board(board)
    console.print("Game over!")
    console.print("Result: " + chess_board.result())

    engine.quit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
