import argparse

from simulator.models.configuration_parser import ConfigurationParser
from simulator.utils import export

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Input file name")
    args = parser.parse_args()
    file_name = args.input

    config_parser = ConfigurationParser(file_name)
    simulation = config_parser.read_config()
    reporter = simulation.run()
    export(reporter)


if __name__ == '__main__':
    main()
