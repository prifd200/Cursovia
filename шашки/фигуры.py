import pygame.draw

from .constants import Rectangle, Grey, Queen
class Piece:
    Padding = 13
    Border = 1
    def __init__(self, lines, col, color):
        self.lines = lines
        self.col = col
        self.color = color
        self.queen = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = Rectangle * self.col + Rectangle // 2
        self.y = Rectangle * self.lines + Rectangle // 2
    def make_queen(self):
        self.queen = True
    def draw(self, win):
        radius = Rectangle // 2 - self.Padding
        pygame.draw.circle(win, Grey, (self.x, self.y), radius + self.Border)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.queen:
            win.blit(Queen, (self.x - Queen.get_width() // 2, self.y - Queen.get_height() // 2))
    def move(self, lines, col):
        self.lines = lines
        self.col = col
        self.calc_pos()
    def __repr__(self):
        return str(self.color)