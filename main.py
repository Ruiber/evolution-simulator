from simulator.models.configuration_parser import ConfigurationParser

def main():
    parser = ConfigurationParser('example-config.json')
    simulation = parser.read_config()


if __name__ == '__main__':
    main()
