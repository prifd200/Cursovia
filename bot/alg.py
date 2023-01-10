from copy import deepcopy
import pygame
from шашки.constants import Grey,White
def minimax(position,depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, White, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, Grey, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board
def get_all_moves(board, color, game):
    moves = []
    mvs = board.check_hits(color)
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        if f"{piece.lines} {piece.col}" in mvs or len(mvs) == 0:
            for move, skip in valid_moves.items():
                temp_board = deepcopy(board)
                temp_piece = temp_board.get_piece(piece.lines, piece.col)
                new_board = simulate_move(temp_piece, move, temp_board, game, skip)
                moves.append(new_board)
    return moves
