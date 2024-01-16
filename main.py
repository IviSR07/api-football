
from typing import Union

from fastapi import FastAPI
from domain.team import Team
from domain.match import Match
from domain.player import Player
from domain.team_repository import TeamRepository
from domain.player_repository import PlayerRepository

'''
Responsabilidad: Enrutar y redirigir la petición a quien corresponda.
'''

app = FastAPI()
print("API FOOTBALL")

## Repositories
repository_teams=TeamRepository()

@app.get("/")
def info():
    return {"Project": "API FOOTBALL"}

@app.get("/matches")
def get_matches():
    real_madrid_vs_almeria=Match("Real Madrid",4,"Almería",2)
    return [real_madrid_vs_almeria]

@app.get("/pichichi")
def get_pichichi():
    return [{
        "name": "Benzema",
        "team": "Real Madrid",
        "goals": 8
    },
    {
        "name": "Modric",
        "team": "Real Madrid",
        "goals": 4
    }]

@app.get("/general_clasification")
def get_general_clasification():
    return [{
        "number": 1,
        "name": "Barcelona",
        "points": 85
    },{
        "number": 2,
        "name": "Real Madrid",
        "points": 71        
    }]

@app.get("/teams")
def get_teams():
    return repository_teams.get()

@app.get("/random")
def get_teams():
    # This is a use case:
    cosa=Team("Iván","Su casa")
    repository_teams.add(cosa)
    return repository_teams.get()

@app.get("/players")
def get_players():
    repository = PlayerRepository()
    players = repository.get()
    name_players=[]
    for player in players:
        name_players.append(player.name)
