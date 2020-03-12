from statsXNAT import dataFetcher

class Formatter:

    data = None   # Data Fetcher Object

    # Passing the name and password to fetcher object
    def __init__(self, name, password, instance_url):

        self.data = dataFetcher.Fetcher(name, password, instance_url)


    def stats(self):

        # Show the overall data counts present on XNAT 

        projects_table = self.data.get_projects()
        subjects_table = self.data.get_subjects()
        experiments_table = self.data.get_experiments()

        # Counter variable for different fields

        counter_left_hand = 0
        counter_right_hand = 0
        counter_unknown_hand = 0
        counter_male = 0
        counter_female = 0
        counter_unknown = 0

        # Looping through each subject to get the required count
        if(subjects_table != None):
            for subject in subjects_table:

                gender = subject['gender_text']
                hand = subject['handedness_text']

                if(gender == 'M'):
                    counter_male = counter_male + 1
                elif(gender == 'F'):
                    counter_female = counter_female + 1
                else:
                    counter_unknown = counter_unknown + 1

                if(hand == 'R'):
                    counter_right_hand = counter_right_hand + 1
                elif(hand == 'L'):
                    counter_left_hand = counter_left_hand + 1
                else:
                    counter_unknown_hand = counter_unknown_hand + 1

            # Making a list to be returned to the flask app for jinja

            return [len(projects_table), 
                    len(subjects_table), 
                    len(experiments_table), 
                    counter_left_hand, 
                    counter_right_hand,
                    counter_unknown, 
                    counter_male, 
                    counter_female, 
                    counter_unknown ]
        else:
            print("Please check network connection")
            print("Please check username or password in configuration file")
            return None