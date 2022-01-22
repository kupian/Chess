from hashlib import new


class Board:
    def __init__(self):
        self.pieces = []

    def Print(self):
        for piece in self.pieces:
            print(piece.type, ":", piece.position)

    def AddPiece(self, piece):
        self.pieces.append(piece)
        print("Added piece of type", piece.type, "at position", piece.position)

    def ValidateMove(self, piece, position):
        pass
        # TODO check if move is valid

        ### Check if position is valid for piece type. (straight line for rook, l shape for knight etc)

        ### Check if move places king under check

        ### Check if move passes through another piece (only allowed for knight)

        ### Check if move lands on another piece and get colour (same colour is illegal, opponent means capture)


class Piece:
    def __init__(self, type, colour, position):
        self.type = type
        self.colour = colour
        self.position = position

board = Board()
board.AddPiece(Piece("Pawn", "White", [0,0]))
board.Print()
