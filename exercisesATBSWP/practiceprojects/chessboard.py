import sys

perfect_board = {
    '1a': '', '2a': '', '3a': '', '4a': '', '5a': '', '6a': '', '7a': '', '8a': '',
    '1b': '', '2b': '', '3b': '', '4b': '', '5b': '', '6b': '', '7b': '', '8b': '',
    '1c': '', '2c': '', '3c': '', '4c': '', '5c': '', '6c': '', '7c': '', '8c': '',
    '1d': '', '2d': '', '3d': '', '4d': '', '5d': '', '6d': '', '7d': '', '8d': '',
    '1e': '', '2e': '', '3e': '', '4e': '', '5e': '', '6e': '', '7e': '', '8e': '',
    '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '', '7f': '', '8f': '',
    '1g': '', '2g': '', '3g': '', '4g': '', '5g': '', '6g': '', '7g': '', '8g': '',
    '1h': '', '2h': '', '3h': '', '4h': '', '5h': '', '6h': '', '7h': '', '8h': ''
}


board = {
    '1a': 'wpawn', '2a': '', '3a': 'brook', '4a': '', '5a': '', '6a': '', '7a': '', '8a': '',
    '1b': '', '2b': 'wbishop', '3b': '', '4b': 'wbishop', '5b': '', '6b': '', '7b': '', '8b': '',
    '1c': 'wpawn', '2c': '', '3c': '', '4c': 'bbishop', '5c': '', '6c': 'wqueen', '7c': '', '8c': '',
    '1d': '', '2d': 'wpawn', '3d': '', '4d': '', '5d': '', '6d': 'bpawn', '7d': '', '8d': '',
    '1e': 'wpawn', '2e': '', '3e': 'wking', '4e': '', '5e': '', '6e': '', '7e': '', '8e': '',
    '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '', '7f': '', '8f': '',
    '1g': '', '2g': 'bbishop', '3g': '', '4g': 'bpawn', '5g': '', '6g': '', '7g': '', '8g': '',
    '1h': 'bking', '2h': '', '3h': '', '4h': 'bpawn', '5h': 'bqueen', '6h': '', '7h': '', '8h': ''
}


def check_board(the_board):
    wking = list(the_board.values()).count('wking')
    wqueen = list(board.values()).count('wqueen')
    wbishop = list(board.values()).count('wbishop')
    wknight = list(board.values()).count('wknight')
    wrook = list(board.values()).count('wrook')
    wpawn = list(board.values()).count('wpawn')
    bking = list(the_board.values()).count('bking')
    bqueen = list(board.values()).count('bqueen')
    bbishop = list(board.values()).count('bbishop')
    bknight = list(board.values()).count('bknight')
    brook = list(board.values()).count('brook')
    bpawn = list(board.values()).count('bpawn')
    total_pieces = list(board.values())
    empty_pieces = total_pieces.count('')
    pieces = 64
    pieces -= empty_pieces
    white_pieces = 0
    black_pieces = 0
    testing_positions_amount = len(list(the_board.keys()))
    perfect_positions_amount = len(list(perfect_board.keys()))

    for i in range(1):
        valid_board = True
        if wking != 1:
            print("Too many white kings.")
            valid_board = False
        if wqueen > 1:
            print("Too many white queens.")
            valid_board = False
        if wbishop > 2:
            print("Too many white bishops.")
            valid_board = False
        if wknight > 2:
            print("Too many white knights.")
            valid_board = False
        if wrook > 2:
            print("Too many white rooks.")
            valid_board = False
        if wpawn > 8:
            print("Too many white pawns.")
            valid_board = False
        if bking != 1:
            print("Too many black kings.")
            valid_board = False
        if bqueen > 1:
            print("Too many black queens.")
            valid_board = False
        if bbishop > 2:
            print("Too many black bishops.")
            valid_board = False
        if bknight > 2:
            print("Too many black knights.")
            valid_board = False
        if brook > 2:
            print("Too many black rooks.")
            valid_board = False
        if bpawn > 8:
            print("Too many black pawns.")
            valid_board = False
        if pieces > 32:
            print("Too many pieces on the board.")
            valid_board = False
        for piece in total_pieces:
            if piece and piece[0] not in ('w', 'b'):
                print("You have a piece in your board that is neither white or black.")
                valid_board = False

            if piece and piece[1:] not in ('king', 'queen', 'bishop', 'knight', 'rook', 'pawn'):
                print(f"The piece '{piece}' is not a valid type of chess piece.")
                valid_board = False
        for piece in total_pieces:
            if piece.startswith('w'):
                white_pieces += 1
                if white_pieces > 16:
                    print("Too many white pieces.")
                    valid_board = False
                    break
            if piece.startswith('b'):
                black_pieces += 1
                if black_pieces > 16:
                    print("Too many black pieces. ")
                    valid_board = False
                    break
        if testing_positions_amount > perfect_positions_amount:
            print("You have either too many positions on your board.")
        if testing_positions_amount < perfect_positions_amount:
            print("You have too less positions on your board.")
        if the_board.keys() != perfect_board.keys():
            print("You do not have valid key entries.")
        if valid_board:
            print("Your board is valid. Good work.")
        else:
            print("Your board was not valid. Please remake the board and run again.")


check_board(board)