from src import dataFetcher

class Formatter:

    data = dataFetcher.Fetcher()   # Data Fetcher Object

    def projects_formatter(self):

        # Show the important fields of the project

        projects_table = self.data.get_projects()

        if(projects_table != None):
            
            print("PROJECT DETAILS")
            print("Number of project visible are ",len(projects_table))
            print("\n\n\n\n")

            # Looping through each project to show the important fields

            for project in projects_table:

                print("Project Creation Date : ", project['insert_date'])
                print("Project Owner Name: ", project['insert_user'])
                print("Project Name : ", project['name'])
                print("Project Description : ", project['description'])
                print("Project Users : ", project['project_users'].split('<br/>'))
                print("Project Visibility : ", project['project_access']) 
                print("Project Members : ", project['project_members'].split('<br/>'))
                print("Project Collaborators : ", project['project_collabs'].split('<br/>'))
                print("\n\n\n\n")

        else:
            print("Please check network connection")
            print("Please check username or password in your configuration file")


    def subjects_formatter(self): 

        # Show the the important fields of subjects

        subjects_table = self.data.get_subjects()

        if(subjects_table != None):
            
            print("SUBJECT DETAILS")
            print("Number of subjects visible are ", len(subjects_table))
            print("\n\n\n\n")

            # Looping through each subject to show the important fields

            for subject in subjects_table:

                print("Subject Creation Date : ", subject['insert_date'])
                print("Subject Creator Name: ", subject['insert_user'])
                print("Subject associated with ",subject['project'],"project")
                print("Subject Gender ", subject['gender_text'])
                print("Subject Handedness : ", subject['handedness_text'])
                print("Subject Date of Birth : ", subject['dob'])
                print("Subject Education : ", subject['educ']) 
                print("Subject SES : ", subject['ses'])
                print("Subject Race : ", subject['race'])
                print("Subject Ethnicity : ", subject['ethnicity'])
                print("\n\n\n\n")

        else:
            print("Please check network connection")
            print("Please check username or password in your configuration file")


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

            return [len(projects_table), len(subjects_table), len(experiments_table), 
                    counter_left_hand, counter_right_hand, counter_unknown, 
                    counter_male, counter_female, counter_unknown]
        else:
            print("Please check network connection")
            print("Please check username or password in configuration file")