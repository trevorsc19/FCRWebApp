"""
This is different from insert_into_database.py.  This file takes a csv that was generaetd randomly on mockaroo.com
"""
# python manage.py shell < insert_mock_data.py

class FakeData:

    first_names = []
    last_names = []
    birthdays = []
    usernames = []
    email_prefix = ["@aol.com", "@gmail.com", "@outlook.com", "@yahoo.com"]

    # get all the usernames from the CSV
    def __init__(self):
        print("in constructor")
        self.first_names, self.last_names, self.birthdays = self.fill_name_lists()
        self.usernames = self.fill_usernames_list()
    
    def insert_mock_data(self):
        import csv
        from profile.models import Profile
        from django.db import connection
        from django.contrib.auth.models import User
        from profile import definitions
        import random
        import pycountry
        from faker import Faker
        from datetime import datetime


        #self.delete_all_users_except_admins()

        fake = Faker(['en_US']) 

        for i in range(0, 1000):
            first_name = fake.first_name()
            last_name = fake.last_name()
            
            # get first character of first name, full last name, 4 random numbers
            nums = ''.join([str(random.randint(0,9)) for p in range(0,4)])
            email = first_name[0][:1].lower()+last_name+nums+random.choice(self.email_prefix)

            # 1994-12-21

            fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115).strftime('%Y-%m-%d')
            country = random.choice(list(pycountry.countries)).name
            # Create a user that will go in auth_user table
            user_one_to_one = self.create_random_user(email_from_profile_object=email)
            profile = Profile(user=user_one_to_one, first_name=first_name, last_name=last_name, email=email, birth_date=birth_date, country=country)
            #print(profile)
            profile.save()

    def create_random_user(self, email_from_profile_object):
        import csv
        from django.contrib.auth.models import User
        from profile.models import Profile
        import random

        username = random.choice(self.usernames)
        self.usernames.remove(username)

        password = User.objects.make_random_password()
        #Make sure that the profile object and user it is tied to have the same email
        user = User.objects.create_user(username, email_from_profile_object, password)
        return userqq
    
    def fill_usernames_list(self, num_of_usernames=1000):
        import csv 
        from profile import definitions

        usernames = []
        
        with open(definitions.USERNAME_DATA) as csvReader:
            reader = csv.DictReader(csvReader)

            for i, row in enumerate(reader):
                usernames.append(row['username'])
                if (i >= num_of_usernames):
                    break
        return usernames
                       
    def delete_all_users_except_admins(self):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM \"auth_user\";""")
           

            for row in cursor.fetchall():
                # delete the one-to-one relationship
                id = row[0]
                cursor.execute("""
                    UPDATE \"profile_table\" SET user_id = NULL WHERE user_id = (%s);""", [id])

            
            cursor.execute("DELETE FROM auth_user WHERE is_superuser IS FALSE")
            for row in cursor.fetchall():
                print(row[0]) # should print number of deleted rows
            
            

        # Can also Use Django ORM
        """
        # Delete all users that aren't an admin
        Users = User.objects.all()
        for user in Users:
            if user.is_superuser:
                print(user.username + " is a superuser")
            else:
                pass
                # user.delete()
        """

    def delete_all_profiles(self):
        from profile.models import Profile

        for p in Profile.objects.all():
            p.delete()



    def run_custom_sql(self):
        from django.db import connection 

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM \"auth_user\";""")

            for row in cursor.fetchall():
                print(row[3])
                
            cursor.execute("""
            SELECT * FROM \"auth_user\" LIMIT 1;""")
            
            for row in cursor.fetchall():
                print(row[3])

            
    
fake_data = FakeData()
#csvTest.delete_all_users_except_admins()
csvTest.insert_mock_data()


