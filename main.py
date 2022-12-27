import pygame
from шашки.constants import WIDTH, HEIGHT, Rectangle, White
from шашки.ходы import Game
from PyQt5 import uic
from shifr import *
from PyQt5.QtWidgets import QApplication
from bot.alg import minimax
import sys
Form, Window = uic.loadUiType("Winner.ui")
app = QApplication([])
window1 = Window()
form1 = Form()
form1.setupUi(window1)
Form2, Window2 = uic.loadUiType("main.ui")
window2 = Window2()
form2 = Form2()
form2.setupUi(window2)
window2.show()
Form3, Window3 = uic.loadUiType("регистрация.ui")
window3 = Window3()
form3 = Form3()
form3.setupUi(window3)
Form4, Window4 = uic.loadUiType("выход.ui")
window4 = Window4()
form4 = Form4()
form4.setupUi(window4)
FPS = 60

def make_move(pos):
    x, y = pos
    lines = y // Rectangle
    col = x // Rectangle
    return lines, col
def auth():
    window3.close()
    window2.show()
    d = open("data.txt", "r+", encoding='UTF-8')
    if f"логин: {encrypt(form2.lineEdit.displayText())}\nпароль: {encrypt(form2.lineEdit_2.displayText())}\n" in d.read() and form2.lineEdit_2.displayText():
        main()
    else:
        form2.plainTextEdit.setPlainText("Неверный логин или пароль")
    d.close()
def reg():
    window3.show()
    window2.close()
    def du():
        if form3.lineEdit_2.displayText() != " " and form3.lineEdit_3.displayText() != " ":
            data_read = open("data.txt", "r+", encoding='UTF-8')
            if f"логин: {encrypt(form3.lineEdit_2.displayText())}\n" in data_read.read():
                form3.lineEdit.setText("Пользователь уже существует")
            elif form3.lineEdit_2.displayText() != "" and form3.lineEdit_3.displayText() != "":
                data_add = open("data.txt", "a+", encoding='UTF-8')
                data_add.write(f"\nлогин: {encrypt(form3.lineEdit_2.displayText())}\nпароль: {encrypt(form3.lineEdit_3.displayText())}\n")
                data_add.close()
                data_read.close()
                window3.close()
                main()
            data_read.close()
    form2.plainTextEdit.setPlainText("Главная")
    form3.pushButton_2.clicked.connect(du)
    form3.pushButton.clicked.connect(auth)
form2.pushButton_2.clicked.connect(reg)
form2.pushButton.clicked.connect(auth)

def main():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Английские Шашки")
    window2.close()
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        if game.turn == White:
            value, new_board = minimax(game.get_board(), 3, White, game)
            game.bot(new_board)
        if game.winner() != None:
            form1.lineEdit.setText(f"Победитель: {game.winner()}")
            window1.show()

            def restart():
                window1.close()
                main()
                form1.pushButton_2.clicked.connect()
            def ext():
                window4.show()

                def nope():
                    window4.close()
                def yep():
                    window4.close()
                    window1.close()
                    window2.show()
                form4.pushButton.clicked.connect(yep)
                form4.pushButton_2.clicked.connect(nope)

            form1.pushButton.clicked.connect(ext)
            form1.pushButton_2.clicked.connect(restart)
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
sys.exit(app.exec_())

