import pygame
from .constants import Grey, White, Blue, Rectangle
from шашки.board import Board
class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = Grey
        self.valid_moves = {}
        self.win = win
    def update(self):
        self.board.draw(self.win)
        self.draw_moves(self.valid_moves)
        pygame.display.update()
    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = Grey
        self.valid_moves = {}
    def winner(self):
        return self.board.winner()
    def select(self, lines, col):
        mvs = self.board.check_hits(self.turn)
        if self.selected:
            result = self.move(lines, col)
            if not result:
                self.selected = None
                self.select(lines, col)
        piece = self.board.get_piece(lines, col)
        if piece != 0 and piece.color == self.turn and (f"{lines} {col}" in mvs and len(mvs) != 0 or len(mvs) == 0):
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def move(self, lines, col):
        piece = self.board.get_piece(lines, col)
        if self.selected and piece == 0 and (lines, col) in self.valid_moves:
            self.board.move(self.selected, lines, col)
            skipped = self.valid_moves[(lines, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_moves(self, moves):
        for move in moves:
            lines, col = move
            pygame.draw.circle(self.win, Blue, (col * Rectangle + Rectangle // 2, lines * Rectangle + Rectangle // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == Grey:
            self.turn = White
        else:
            self.turn = Grey

    def get_board(self):
        return self.board

    def bot(self, board):
        self.board = board
        self.change_turn()



