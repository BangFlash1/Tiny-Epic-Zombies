from .room import Room
from .graph import Graph
from .player import Player
from .constants import ROOMS

class RoomManager: #  RoomManager is for the purpose of adding and removing entities from rooms
    def __init__(self, graph: Graph):
        self.rooms = [Room(i) for i in range(ROOMS)]
<<<<<<< Updated upstream
        self.players = []
        self.enemies = []
        self.__graph = graph

    def addZombie(self, roomID, zombie):
        self.rooms[roomID].enemies.append(Zombie(len(self.enemies)))
        self.enemies.append(zombie)
=======
        self.players = {}
        self.enemies = []
        self.__graph = graph

# addPlayer/addZombie: Adds each player/zombie to a dictionary with the keys being consecutive numbers starting at 0 and the values being the player objects.
>>>>>>> Stashed changes

    def addPlayer(self, playerName, roomID):
        self.players.append(Player(playerName))
        player = self.players[-1]
        player.room = self.rooms[roomID]
        self.rooms[roomID].players.append(player)

    def movePlayer(self, playerID, newRoom):
        player = self.players[playerID]
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