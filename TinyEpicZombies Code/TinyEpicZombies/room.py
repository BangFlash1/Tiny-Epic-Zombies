class Room:
    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)
    
    def returnPlayers(self):
        return [player.name for player in self.players]