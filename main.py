
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
    real_sociedad=("Real Sociedad")
    athletic_club_de_bilbao=Team("Athletic Club de Bilbao")
    betis=Team("Betis")
    return [real_madrid,barcelona,almeria,atletico_de_madrid,sevilla,real_sociedad,athletic_club_de_bilbao,betis]


@app.get("/matches")
def get_matches():
    real_madrid_vs_almeria=Match("Real Madrid","Almería")
    return [{"local":"Real Madrid","visitante":"Almería"}]
