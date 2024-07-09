import pygame
from .board import Board
from .constants import PLAYER_COLOUR_1, PLAYER_COLOUR_2, BLACK, WHITE, SQUARE_SIZE

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw_black(self.win)
        self.board.draw(self.win)
        if self.selected:
            if self.selected.colour == self.turn:
                self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER_COLOUR_1
        self.valid_moves = {}
    
    def reset(self):
        self._init()
    
    def select(self, row, col, win):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col, win)

        player = self.board.get_square(row, col)
        if player != 0 and player.colour == self.turn:
            self.selected = player
            self.valid_moves = self.board.get_valid_moves(player)
            return True

        return False
    
    
    def _move(self, row, col):
        player = self.board.get_square(row, col)
        if self.selected and player == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
        else:
            return False
    
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, WHITE,(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
        # if self.selected == None:
        #     self.win.fill(BLACK)
    
    def change_turn(self):
        if self.turn == PLAYER_COLOUR_1:
            self.turn = PLAYER_COLOUR_2
        else:
            self.turn = PLAYER_COLOUR_1