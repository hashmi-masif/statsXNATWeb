# file for fetching data from CENTRAL XNAT

from pyxnat import Interface

class Fetcher:

    SELECTOR = None

    # Initializing the central interface object in the constructor
    def __init__(self, name, password):

        SELECTOR = Interface(server = 'https://central.xnat.org',
                            user = name,
                            password = password   )

        self.SELECTOR = SELECTOR

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