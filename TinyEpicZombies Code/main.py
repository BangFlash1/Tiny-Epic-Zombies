import pygame
from TinyEpicZombies.constants import WIDTH, HEIGHT, ROWS, WHITE, PLAYER_COLOUR_1, COLS, SQUARE_SIZE, PLAYER_COLOUR_2, RIGHT_GUI
from TinyEpicZombies.game import Game
from TinyEpicZombies.player import Player

FPS = 60

WIN = pygame.display.set_mode((WIDTH + RIGHT_GUI, HEIGHT))
pygame.display.set_caption("Tiny Epic Zombies")

def mouseRowCol(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    player = Player(6, 4, PLAYER_COLOUR_1, WHITE)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    while 1:
                        pygame.quit()
                    pass
                
                if event.key == pygame.K_t:
                    game.board.addPlayer(player)
                    
                if event.key == pygame.K_r:
                    game.reset()
            
                if event.key == pygame.K_p:
                    pos = pygame.mouse.get_pos()
                    row, col = mouseRowCol(pos)
                    player2 = Player(row, col, PLAYER_COLOUR_2, WHITE)
                    game.board.addPlayer(player2)
                
                if event.key == pygame.K_c:
                    game.change_turn()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = mouseRowCol(pos)
                if row > (ROWS - 1) or col > (COLS - 1):
                    pass
                else:
                    game.select(row, col, WIN)
            
        
        game.update()

    pygame.quit()

main()