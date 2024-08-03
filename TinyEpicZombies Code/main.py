import pygame
from TinyEpicZombies.constants import ROOMS, SQUARE_SIZE
from TinyEpicZombies.player import Player
from TinyEpicZombies.game import Game

FPS = 60

WIN = None
PLAYERS = 1
pygame.display.set_caption("Tiny Epic Zombies")

p1 = Player("Lara")

def main():
    run = True
    game = Game(WIN, ROOMS)
    game.roomManager.addPlayer(p1, 0)
    game.graph.addEdge(0, 1, 1)
    game.roomManager.movePlayer(p1, 1)

main()