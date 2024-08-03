from .graph import Graph

class Game:
    def __init__(self, win, rooms, players):
        self.win = win
        self.graph = Graph(rooms, players)

    def update(self):
        pass

    def reset(self):
        self._init()