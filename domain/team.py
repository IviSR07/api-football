class Team:

    def __init__(self,name: str,stadium: str="",division: int=1):
        self.name: str = name
        self.stadium: str = stadium
        self.division: int = division
    
    def change_name(self, name: str):
        self.name: str = name

    def change_stadium(self, stadium: str):
        self.stadium = stadium
        
    def up_division(self):
        #TODO: check division
        self.division = self.division - 1
        
    def down_division(self):
        #TODO: check division
        self.division = self.division + 1