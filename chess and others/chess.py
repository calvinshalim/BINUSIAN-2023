Problem 1: Chess
Given a Knights  / King / Rook position on the board using notation,
give the list of all possible moves in the board
(Assume the board is empty)
Input : B1
Output: - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        + - + - - - - -
        - - - + - - - -
        - o - - - - - -

steps:
    1. input X
    2. determine output : B3 etc
    3. create function to draw empty board
    4. create function to place the pieces
#%% KING MOVES IN CHESS
class Chess(object):
    X = 0
    Y = 0

    def __init__(self, size):
        parsed = size.split("x")
        self.sizeX = int(parsed[0])
        self.sizeY = int(parsed[1])
        self.chessboard = self.makechessboard()

    def makechessboard(self):
        return [[0 for _ in range(self.sizeX)] for _ in range(self.sizeY)]

    def printchessboard(self):
        for y in self.chessboard:
            for x in y:
                if x == 0:
                    print("- ", end="")
                elif x == 1:
                    print("o ", end="")
                else:
                    print("+ ", end="")
            print()

    def chessposition(self, move):
        self.Y = len(self.chessboard)-int(move[1:])
        self.X = ord(move[0])-65
        self.chessboard[self.Y][self.X] = 1 

    def possiblemoves(self):
        for move in [(self.X, self.Y+1), (self.X+1, self.Y+1), (self.X+1, self.Y), 
                     (self.X+1, self.Y-1), (self.X, self.Y-1), (self.X-1, self.Y-1), 
                     (self.X-1, self.Y), (self.X-1, self.Y+1)]: 
           try:
                if ((move[1] >= 0) and (move[1] < self.sizeX)) and ((move[0] >= 0) and (move[0] < self.sizeY)):
                    self.chessboard[move[1]][move[0]] = 2 
           except IndexError:
                pass 

chess = Chess(input("Enter chessboard length and width(8x8): "))
chess.chessposition(input("input your chess position(B3,etc): "))
chess.possiblemoves()
chess.printchessboard()
#%%