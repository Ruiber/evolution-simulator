from simulator.models.configuration_parser import ConfigurationParser
from simulator.utils import export

def main():
    parser = ConfigurationParser('example-config.json')
    simulation = parser.read_config()
    reporter = simulation.run()
    export(reporter)


if __name__ == '__main__':
    main()
