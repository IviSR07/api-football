class Team:

    def __init__(self,name,stadium="",division=1):
        self.name= name
        self.stadium= stadium
        self.division= division
    
    def change_name(self, name):
        self.name = name

    def change_stadium(self, stadium):
        self.stadium = stadium
        
    def up_division(self):
        self.division = self.division - 1
        
    def down_division(self):
        self.division = self.division + 1