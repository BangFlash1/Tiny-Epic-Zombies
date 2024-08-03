class Room:
    def __init__(self, roomID):
        self.roomID = roomID
        self.players = []
        self.enemies = []

    def addPlayer(self, player):
        self.players.append(player)
    
    def returnPlayers(self):
        return [player.name for player in self.players]