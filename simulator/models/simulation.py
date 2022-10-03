class Simulation:
    def __init__(self, species_groups, total_rounds):
        self.species_groups = species_groups
        self.total_rounds = total_rounds
    

    def run(self):
        for current_round in self.total_rounds:
            self.run_round()


    def run_round(self):
        pass
