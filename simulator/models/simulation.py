class Simulation:
    def __init__(self, species_groups, total_rounds, population, mutation_matrix):
        self.species_groups = species_groups
        self.total_rounds = total_rounds
        self.population = population
        self.mutation_matrix = mutation_matrix
    

    def run(self):
        for current_round in self.total_rounds:
            self.run_round()


    def run_round(self):
        pass
