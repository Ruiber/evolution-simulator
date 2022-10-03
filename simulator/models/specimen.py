from random import random


class Specimen():
    def __init__(self, species):
        self.species = species
        self.food = 0


    def decide_fate(self):
        survival_probability = min(1, self.food)
        reproduction_probability = max(0, self.food - 1)

        survival = random() < survival_probability
        reproduction = random() < reproduction_probability

        if not survival:
            self.species.death()
        if reproduction:
            self.species.birth()

        self.food = 0

        return (survival, reproduction)
