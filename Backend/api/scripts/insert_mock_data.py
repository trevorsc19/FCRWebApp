"""
This is different from insert_into_database.py.  This file takes a csv that was generaetd randomly on mockaroo.com
"""
# python manage.py shell < insert_mock_data.py

class CSV:

    list_of_users = []

    # get all the usernames from the CSV
    def __init__(self):
        print("in constructor")
        self.list_of_users = self.get_random_usernames()

    def insert_mock_data(self):
        
        import csv
        from api.models import Person
        from django.db import connection
        from django.contrib.auth.models import User
        from api import definitions

        users = User.objects.all()
        print(type(users))

        # Delete entries in person table
        for p in Person.objects.all():
            p.delete()

        # if there is more than just 'TheAbsoluteAdmin', then delete everything
        # or can check username and only delete if its not 'TheAbsoluteAdmin'
        if len(users) > 1:
            for user in users:
                print(user.password)
            print("deleting users")
            self.delete_most_users()
        else:
            print("The only user is ", users[0].username)

        # create users from csv file 
        with open(definitions.PERSON_DATA) as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                first_name = row['first_name']
                last_name = row['last_name']
                email = row['email']
                birth_date = row['birth_date']
                country = row['country']
                #args = [first_name, last_name, email, birth_date, country]
                #person_to_save_to_database = Person(**args)
                
                # Create a user that will go in auth_user table. Will make one-to-one relationship with Person object
                user_to_connect = self.create_random_user(email_from_person_object=email)

                print("adding user")
                person_to_save_to_database = Person(user=user_to_connect, first_name=first_name, last_name=last_name, email=email, birth_date=birth_date, country=country)
                person_to_save_to_database.save()
            
        
    from string import ascii_lowercase, digits

    # passing in email from mock_data.csv
    # default argument has to come after non-default argument
    def create_random_user(self, email_from_person_object, length_of_users_list=1000):

        import csv
        from django.contrib.auth.models import User
        from api.models import Person

        username = self.list_of_users[0]['username']
        # so we don't get any repeats
        del self.list_of_users[0] 

        password = User.objects.make_random_password()
        user = User.objects.create_user(username, password)
        # Now person object and the user it is tied to will have the same email 
        user.email = email_from_person_object
        user.save()
        return user

    # read in usernames from csv file. The csv file was randomly generated from mockaroo
    # make default value
    def get_random_usernames(self, num_of_usernames=1000):
        
        usernames = []

        import csv
        from random import choice
        from django.contrib.auth.models import User
        from api import definitions

        with open(definitions.USERNAME_DATA) as csvFile:
            reader = csv.DictReader(csvFile)
            for i, row in enumerate(reader):
                usernames.append(row)
                if(i >= num_of_usernames):
                    break
        return usernames
        

    def create_random_users(self):

        from django.contrib.auth.models import User
        from api.models import Person
        
        for i in range(len(Person.objects.all())):
            first_name = ""
            last_name = ""
            email = ""
            username = self.generate_random_username()
            password = User.objects.make_random_password()

            user = User.objects.create_user(username, password)

            user.save()

    def delete_most_users(self):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM \"auth_user\";""")
           
            for row in cursor.fetchall():
                # we have to delete the user from the person table (one to one relationship)
                id = row[0]
                cursor.execute("""
                    UPDATE \"PERSON_TABLE\" SET user_id = NULL WHERE user_id = (%s);""", [id])
            
            cursor.execute("DELETE FROM auth_user WHERE username NOT IN ('TheAbsoluteAdmin');")
            #print(len(cursor.fetchall()))

           #DELETE FROM table WHERE id NOT IN ( 2 )
        
    def sql_test(self):
        from django.db import connection
        from django.contrib.auth.models import User

        #users = User.objects.all()
        #print(type(users))

        
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM "PERSON_TABLE" WHERE id=6250;""")
            
            for row in cursor.fetchall():
                print(row)
        
        
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

"""
import csv

with open('Cars.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Colour'] == 'blue':
            print(row['ID'] ,row ['Make'],row ['Colour'])
"""