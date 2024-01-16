from domain.player import Player

'''
Responsabilidad: añadir jugadores, obtener la lista de los jugadores.
'''

class PlayerRepository:

    def __init__(self):
        pass

    def add(player: Player):
        pass

    def get(self):
        players=[]
        benzema = Player("Benzema","Real Madrid")
        players.append(benzema)
        vinicius_jr=Player("Vinicius Jr","Real Madrid")
        players.append(vinicius_jr)
        bellingham = Player("Bellingham","Real Madrid")
        players.append(bellingham)
        return players
