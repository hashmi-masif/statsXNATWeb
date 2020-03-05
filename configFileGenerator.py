from pyxnat import Interface
from src import dataFormatter

class ConfigFileGenerator:

    name = ""
    password = ""

    def name_and_pass(self, name, password, test_check=0): # Function for taking input from the users

        if(test_check == 0):     # To check whether network connection is fine 
            self.name = name
            self.password = password
            data = self.generator() 
            return data         # This will return list containing information or None
        else:
            self.name = 'testUser'
            self.password = 'testPassword'
            return None

    def generator(self): # Function for creating the configuration file

        central = Interface(server = 'https://central.xnat.org',
                            user = self.name,
                            password = self.password    )

        central.save_config('ConfigFile/central.cfg')
        print("Configuration file Created...........")

        # Creating the object for formatter

        DATA_FORMATTER = dataFormatter.Formatter()

        stats = DATA_FORMATTER.stats()          # stats() returns the data fetched from formatter
        return stats