from random import shuffle

from simulator.models.specimen import Specimen


class Simulation:
    def __init__(self, species_groups, total_rounds, food_pairs):
        self.species_groups = species_groups
        self.total_rounds = total_rounds
        self.food_pairs = food_pairs
        self.specimens = []
        first_round = dict()
        for species in species_groups:
            first_round[species.name] = species.population
            for _ in range(species.population):
                self.specimens.append(Specimen(species))
        self.reporter = [first_round]
    

    def run(self):
        for _ in range(self.total_rounds):
            self.run_round()
        
        return self.reporter


    def run_round(self):
        allocation = self.allocate_food()

        for food_pair in allocation:
            self.handle_meet(food_pair)

        new_specimens = []
        for specimen in self.specimens:
            survival, reproduction = specimen.decide_fate()
            if not survival:
                self.specimens.remove(specimen)
            if reproduction:
                new_specimens.append(Specimen(specimen.species))

        self.specimens.extend(new_specimens)

        this_round = dict()
        for species in self.species_groups:
            this_round[species.name] = species.population

        self.reporter.append(this_round)


    def allocate_food(self):
        shuffle(self.specimens)
        food_pairs_allocation = [[] for _ in range(self.food_pairs)]
        available_food_pairs = [i for i in range(self.food_pairs)]

        for specimen in self.specimens:
            if len(available_food_pairs):
                shuffle(available_food_pairs)
                chosen_pair = available_food_pairs[0]

                food_pairs_allocation[chosen_pair].append(specimen)
                if len(food_pairs_allocation[chosen_pair]) > 1:
                    available_food_pairs.remove(chosen_pair)
            else:
                break

        return food_pairs_allocation

    
    def handle_meet(self, food_pair):
        #TODO: avaliar como fica a generalização
        if len(food_pair) == 2:
            if food_pair[0].species.aggression == food_pair[1].species.aggression:
                food_pair[0].food = 1 - food_pair[0].species.aggression
                food_pair[1].food = 1 - food_pair[1].species.aggression
            else:
                aggression_sum = food_pair[0].species.aggression + food_pair[1].species.aggression
                food_pair[0].food = 0.5 + food_pair[0].species.aggression / aggression_sum
                food_pair[1].food = 0.5 + food_pair[1].species.aggression / aggression_sum
        elif len(food_pair) == 1:
            food_pair[0].food = 2

