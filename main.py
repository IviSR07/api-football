
from typing import Union

from fastapi import FastAPI
from team import Team
app = FastAPI()
print("API FOOTBALL")

@app.get("/")
def info():
    return {"Project": "API FOOTBALL"}

@app.get("/teams")
def get_teams():
    real_madrid=Team("Real Madrid","Santiago Bernabéu")
    almeria=Team("Almería","Power House Stadium")
    barcelona=Team("Barcelona")
    atletico_de_madrid=Team("Atlético de Madrid")
    sevilla=Team("Sevilla")
athletic_club_de_bilbao=Team("Athletic Club de Bilbao")
    return [real_madrid,barcelona,atletico_de_madrid,almeria,sevilla,athletic_club_de_bilbao]

@app.get("/matches")
def get_matches():
    return [{"local":"Real Madrid","visitante":"Almería"}]
