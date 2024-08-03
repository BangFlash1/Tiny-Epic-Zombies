from .room import Room
from .graph import Graph
from .constants import ROOMS

class RoomManager: #  RoomManager is for the purpose of adding and removing entities from rooms
    def __init__(self, graph: Graph):
        self.rooms = [Room(i) for i in range(ROOMS)]
        self.__graph = graph

    def addPlayer(self, player, roomID):
        player.room = self.rooms[roomID]
        self.rooms[roomID].players.append(player)

    def movePlayer(self, player, newRoom):
        legalMoves = self.generateMoves(player)
        if newRoom in legalMoves:
            player.room.players.remove(player)
            player.room = self.rooms[newRoom]
            player.room.players.append(player)
            print("Move successful")
        else:
            print("Illegal move")

    def generateMoves(self, player):
        startingRoom = player.room.roomID
        legalMoves = []
        for newRoom in range(ROOMS):
            if self.__graph.adjMatrix[startingRoom][newRoom] != -1:
                legalMoves.append(newRoom)
        return legalMoves
