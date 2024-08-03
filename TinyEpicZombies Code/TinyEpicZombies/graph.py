from.constants import ROOMS
from .room import Room
from .player import Player

class Graph:
    def __init__(self, numberOfRooms, players):
        self.__adjMatrix = []
        self.create_adjMatrix(numberOfRooms)
        self.rooms = [Room() for i in range(ROOMS)]

    def create_adjMatrix(self, numberOfRooms):
        self.__adjMatrix = [[-1]*numberOfRooms for i in range(numberOfRooms)]
    
    def addPlayer(self, player, room):
        player.room = room
        room.players.append(player)
    
    def movePlayer(self, player, newRoom):
        player.room.players.remove(player)
        player.room = newRoom
        newRoom.players.append(player)


    def returnAdjMatrix(self):
        return self.__adjMatrix