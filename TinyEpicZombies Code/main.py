import pygame
from TinyEpicZombies.constants import ROOMS, SQUARE_SIZE
from TinyEpicZombies.player import Player
from TinyEpicZombies.game import Game

FPS = 60

WIN = None
PLAYERS = 1
pygame.display.set_caption("Tiny Epic Zombies")

def main():
    run = True
    game = Game(WIN, ROOMS)
    game.roomManager.addPlayer("Lara", 0)
    game.graph.addEdge(0, 1, 1)
    game.roomManager.movePlayer(0, 1)

main()