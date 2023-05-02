
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
    return [real_madrid,barcelona,{"name":"Atlético de Madrid"},almeria]

@app.get("/matches")
def get_matches():
    return [{"local":"Real Madrid","visitante":"Almería"}]
