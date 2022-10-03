class Species:
    def __init__(self, name, aggression, population):
        self.name = name
        self.aggression = aggression
        self.population = population

    
    def death(self):
        self.population -= 1


    def birth(self):
        self.population += 1
