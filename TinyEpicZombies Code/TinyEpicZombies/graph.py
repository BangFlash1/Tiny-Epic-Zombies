from.constants import ROOMS
from .player import Player

# The graph is represented by an adjacency matrix. It contains the 

class Graph:
    def __init__(self, numberOfRooms):
        self.adjMatrix = []
        self.create_adjMatrix(numberOfRooms)
        
    def create_adjMatrix(self, numberOfRooms):
        self.adjMatrix = [[-1]*numberOfRooms for i in range(numberOfRooms)]
    
    def addEdge(self, startingRoomIndex, newRoomIndex, value):
        self.adjMatrix[startingRoomIndex][newRoomIndex] = value

    def returnAdjMatrix(self):
        return self.adjMatrix