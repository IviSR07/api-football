from domain.team import Team
class TeamRepository:

    def __init__(self):
        self.teams = [
            Team("Real Madrid","Santiago Bernabéu"),
            Team("Almería","Power House Stadium"),
            Team("Barcelona"),
            Team("Atlético de Madrid"),
            Team("Sevilla"),
            Team("Real Sociedad"),
            Team("Athletic Club de Bilbao"),
            Team("Betis")
        ]
        pass

    def get(self):        
        return self.teams

    def add(self,team):
        self.teams.append(team)