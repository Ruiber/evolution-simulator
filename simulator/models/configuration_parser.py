import json
import os

from simulator.models.simulation import Simulation
from simulator.models.species import Species


class ConfigurationParser:
    def __init__(self, file_name):
        self.file_name = file_name

    
    def read_config(self) -> Simulation:
        path = os.path.realpath(__file__)
        path = os.path.dirname(path)
        #TODO: make this line independent of OS
        path = path.replace('simulator/models', 'input/' + self.file_name)
        
        with open(path, 'r') as file:
            config = json.load(file)
            rounds = config.get('rounds')

            species_list = config.get('species')
            species_groups = []
            for species in species_list:
                species_groups.append(Species(species.get('birth'), species.get('death'), species.get('reproduction'), species.get('population')))

            mutation = config.get('mutation')
            
            return Simulation(species_groups, rounds, mutation)
