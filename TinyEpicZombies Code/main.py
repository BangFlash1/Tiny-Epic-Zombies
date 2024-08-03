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
    game = Game(WIN, ROOMS, PLAYERS)
    game.graph.addPlayer(p1, game.graph.rooms[0])
    game.graph.movePlayer(p1, game.graph.rooms[1])

main()