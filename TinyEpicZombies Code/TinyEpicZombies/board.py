import pygame
from .constants import BLACK, WHITE, ROWS, COLS, WIDTH, PLAYER_COLOUR_1, PLAYER_COLOUR_2

class Board:
    def __init__(self):
        self.board = []
        self.players_left = 0
        self.zombies = 0
        self.create_board()

    def draw_black(self, win):
        win.fill(BLACK)

    def draw_grid(self, win, rows, width):
        gap = width // rows
        for i in range(rows + 1):
            pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows + 1):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))

    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
    
    def addPlayer(self, player):
        self.board[player.row][player.col] = player
    
    def move(self, player, row, col):
        try:
            self.board[player.row][player.col], self.board[row][col] = self.board[row][col], self.board[player.row][player.col]
            player.move(row, col)
        except AttributeError:
            print(f"No piece at that square: ({player})\n")

    
    def get_square(self, row, col):
        return self.board[row][col]
        

    def draw(self, win):
        self.draw_grid(win, ROWS, WIDTH)
        for row in range(ROWS):
            for col in range(COLS):
                currentSquare = self.board[row][col]
                if currentSquare != 0:
                    currentSquare.draw(win)

    def returnboard(self):
        return self.board
    
    def _traverseLeft(self, player):
        moves = {}
        row = player.row
        for c in range(player.col - 1, -1, -1):
            current = self.board[row][c]
            if current == 0:
                moves[(row, c)] = current
            else:
                break

        return moves

    def _traverseRight(self, player):
        moves = {}
        row = player.row
        for c in range(player.col + 1, ROWS, 1):
            current = self.board[row][c]
            if current == 0:
                moves[row, c] = current
            else:
                break

        return moves

    def _traverseUp(self, player):
        moves = {}
        col = player.col
        for r in range(player.row - 1, -1, -1):
            current = self.board[r][col]
            if current == 0:
                moves[r, col] = current
            else:
                break

        return moves
    
    def _traverseDown(self, player):
        moves = {}
        col = player.col
        for r in range(player.row + 1, COLS, 1):
            current = self.board[r][col]
            if current == 0:
                moves[r, col] = current
            else:
                break
        
        return moves
    
    def get_valid_moves(self, player):
        moves = {} # moves could contain valid move coordinates as the key and probably the number of zombies in the room as the other thing idk

        moves.update(self._traverseLeft(player))
        moves.update(self._traverseRight(player))
        moves.update(self._traverseUp(player))
        moves.update(self._traverseDown(player))

        return moves