class NBAPlayer:
    class PlayerInfo:
        def __init__(self, name, age, school):
            self.name = name
            self.age = age
            self.school = school 
        
        def getName(self):
            return self.name
        
        def getAge(self):
            return self.age
        
        def getSchool(self):
            return self.school
    
    def __init__(self, team, yearsPro, ppg, rpg, apg, height, weight, handedness):
        self.team = team
        self.yearsPro = yearsPro
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg
        self.height = height
        self.weight = weight
        self.handedness = handedness


playerOne = NBAPlayer('GSW', 17, 26.6, 3.6, 4.7, 74, 185, 'Right')

playerOneInfo = NBAPlayer.PlayerInfo('Stephen Curry', 36, "Davidson")

