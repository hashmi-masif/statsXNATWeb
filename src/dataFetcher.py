# file for fetching data from CENTRAL XNAT

from pyxnat import Interface


class Fetcher:

    try: # Checking if the configuration file is created
        SELECTOR = Interface(config = 'ConfigFile/central.cfg')
    except:
        print("Please create the configuration file first")
        exit(1)

    def get_projects(self):

        # Returns a json table with all visible project details or public projects  to user

        try:
            print("Processing............")
            output = self.SELECTOR.select('xnat:projectData').all() 
            return output
        except:
            print("ERROR : Unable to connect to the database")
            return None


    def get_subjects(self):

        # Returns a json table with all visible subjects details or public subjects to the user

        try:
            print("Processing............")
            output = self.SELECTOR.select('xnat:subjectData').all()
            return output
        except:
            print("ERROR : Unable to connect to the database")
            return None

    def get_experiments(self):

        # Returns a json table with all visible project details or public projects to user

        try:
            print("Processing............")
            output = self.SELECTOR.select('xnat:mrSessionData').all()
            return output
        except:
            print("ERROR : Unable to connect to the database")
            return None