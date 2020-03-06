from pyxnat import Interface
from src import dataFormatter

class ConfigFileGenerator:

    name = ""
    password = ""

    def name_and_pass(self, name, password): # Function for taking input from the users

        self.name = name
        self.password = password
        data = self.generator() 
        return data

    def generator(self): # Function for creating the configuration file

        central = Interface(server = 'https://central.xnat.org',
                            user = self.name,
                            password = self.password    )

        central.save_config('../ConfigFile/central.cfg')
        print("Configuration file Created...........")

        # Creating the object for formatter

        DATA_FORMATTER = dataFormatter.Formatter()

        stats = DATA_FORMATTER.stats()          # stats() returns the data fetched from formatter
        return stats