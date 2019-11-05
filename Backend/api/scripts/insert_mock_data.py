"""
This is different from insert_into_database.py.  This file takes a csv that was generaetd randomly on mockaroo.com
"""
# python manage.py shell < insert_mock_data.py

class CSV:

    first_names = []
    last_names = []
    usernames = []

    # get all the usernames from the CSV
    def __init__(self):
        print("in constructor")
        self.first_names, self.last_names = self.fill_name_lists()
        self.usernames = self.fill_usernames_list()
        print(len(self.first_names))
        print(len(self.last_names))
        print(len(self.usernames))

        
    
    def fill_name_lists(self):
        import csv
        from api import definitions

        first_names = []
        last_names = []

        with open(definitions.PERSON_DATA) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                first_name = row['first_name']
                last_name = row['last_name']
                first_names.append(first_name)
                last_names.append(last_name)
        
        return first_names, last_names

    def fill_usernames_list(self, num_of_usernames=1000):
        import csv 
        from api import definitions

        usernames = []
        
        with open(definitions.USERNAME_DATA) as csvReader:
            reader = csv.DictReader(csvReader)

            for i, row in enumerate(reader):
                usernames.append(row)
                if (i >= num_of_usernames):
                    break
        return usernames
                
                
                
        
    def insert_mock_data(self):
        pass

csvTest = CSV()

#csvTest.sql_test()
#csvTest.delete_most_users()
# useres have to be in database before we use their id
#csvTest.create_random_users()
csvTest.insert_mock_data()
#CSV.create_random_users()
#CSV.insert_mock_data()    
#CSV.delete_person_table()

# in Python 3, don't need if __init__ == __main__