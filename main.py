import pygame
from шашки.constants import WIDTH, HEIGHT, Rectangle, Grey
from шашки.ходы import Game
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
Form, Window = uic.loadUiType("Winner.ui")
app = QApplication([])
window1 = Window()
form1 = Form()
form1.setupUi(window1)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Английские Шашки")
def make_move(pos):
    x, y = pos
    lines = y // Rectangle
    col = x // Rectangle
    return lines, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        if game.winner() != None:
            form1.lineEdit.setText(f"Победитель: {game.winner()}")
            window1.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                lines, col = make_move(pos)
                game.select(lines, col)
        game.update()
    pygame.quit()
    window1.close()
    app.exec_()

main()