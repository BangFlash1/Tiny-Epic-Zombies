from .graph import Graph
from .roomManager import RoomManager

class Game:
    def __init__(self, win, rooms):
        self.win = win
        self.graph = Graph(rooms)
        self.roomManager = RoomManager(self.graph)

    def update(self):
        pass

    def reset(self):
        self._init()