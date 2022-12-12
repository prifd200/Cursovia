import pygame
from.constants import Black, WHIT, Lines, Rectangle, Columns, White, Grey
from .фигуры import Piece
class Board:
    def __init__(self):
        self.board = []
        self.grey_left = self.white_left = 12
        self.grey_queen = self.white_queen = 0
        self.create_board()
    def draw_cubes(self, win):
        win.fill(Black)
        for lines in range(Lines):
            for col in range (lines % 2, Columns, 2):
                pygame.draw.rect(win, WHIT, (lines*Rectangle, col*Rectangle, Rectangle, Rectangle))

    #Фигуры
    def move(self, Piece, lines, col ):
        self.board[Piece.lines][Piece.col], self.board[lines][col] =self.board[lines][col], self.board[Piece.lines][Piece.col]
        Piece.move(lines, col)
        if lines == Lines - 1 or lines == 0:
            Piece.make_queen()
            if Piece.color == White:
                self.white_queen += 1
            else:
                self.grey_queen += 1
    def get_piece(self, lines, col):
        return self.board[lines][col]

    def create_board(self):
        for lines in range(Lines):
            self.board.append([])
            for col in range(Columns):
                if col % 2 == ((lines + 1) % 2):
                    if lines < 3:
                        self.board[lines].append(Piece(lines,col,White))
                    elif lines > 4:
                        self.board[lines].append(Piece(lines,col,Grey))
                    else:
                        self.board[lines].append(0)
                else:
                    self.board[lines].append(0)
    def draw(self, win):
        self.draw_cubes(win)
        for lines in range(Lines):
            for col in range(Columns):
                piece = self.board[lines][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.lines][piece.col] = 0
            if piece != 0:
                if piece.color == Grey:
                    self.grey_left -= 1
                else:
                    self.white_left -= 1
    def winner(self):
        if self.grey_left <= 0:
            return "Белые"
        elif self.white_left <= 0:
            return "Cерые"
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        lines = piece.lines
        if piece.color == Grey or piece.queen:
            moves.update(self.Left(lines - 1, max(lines - 4, -1), -1, piece.color, left ))
            moves.update(self.Right(lines - 1, max(lines - 4, -1), -1, piece.color, right))
        if piece.color == White or piece.queen:
            moves.update(self.Left(lines + 1, min(lines + 4, Lines), 1, piece.color, left))
            moves.update(self.Right(lines + 1, min(lines + 4, Lines), 1, piece.color, right))
        return moves

    def Left(self, start, stop,step, color, left, skipped=[]):
        moves = {}
        last = []
        for i in range (start,stop,step):
            if left < 0:
                break
            current = self.board[i][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i,left)] = last + skipped
                else:
                    moves[(i, left)] = last
                if last:
                    if step == -1:
                        lines = max(i-3, 0)
                    else:
                        lines = min(i+3, Lines)
                    moves.update(self.Left(i + step, lines, step, color, left-1, skipped=last))
                    moves.update(self.Right(i + step, lines, step, color, left + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves
    def Right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for i in range(start, stop, step):
            if right >= Columns:
                break
            current = self.board[i][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i, right)] = last + skipped
                else:
                    moves[(i, right)] = last
                if last:
                    if step == -1:
                        lines = max(i - 3, 0)
                    else:
                        lines = min(i + 3, Lines)
                    moves.update(self.Left(i + step, lines, step, color, right - 1, skipped=last))
                    moves.update(self.Right(i + step, lines, step, color, right + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves


