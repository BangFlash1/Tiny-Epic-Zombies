from .constants import PLAYER_COLOUR_1, PLAYER_COLOUR_2, SQUARE_SIZE
import pygame

class Player:

    PADDING = 10
    BOARDER = 2

    def __init__(self, row, col, colour, outline):
        self.row = row
        self.col = col
        self.type = type
        self.room = None
        self.colour = colour
        self.outline = outline

        if self.type == "p":
            self.room = 0 # for later, 0 will represent the starting room

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.outline, (self.x, self.y), radius + self.BOARDER)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
