"""
This is different from insert_into_database.py.  This file takes a csv that was generaetd randomly on mockaroo.com
"""
# python manage.py shell < insert_mock_data.py
import time;

class FakeData:

    usernames = []
    email_prefix = ["@aol.com", "@gmail.com", "@outlook.com", "@yahoo.com"]

    # get all the usernames from the CSV
    def __init__(self):
        from django.db import connection

        print("in constructor")
        self.usernames = self.fill_usernames_list()
       
    
    def insert_mock_data(self):
        import csv
        from profile.models import Profile
        from django.db import connection
        # from django.contrib.auth.models import User
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
            birth_date = fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115).strftime('%Y-%m-%d')
            country = random.choice(list(pycountry.countries)).name
            # Create a user that will go in auth_user table
            user_one_to_one = self.create_random_user(email_from_profile_object=email)
            profile = Profile(user=user_one_to_one, first_name=first_name, last_name=last_name, email=email, birth_date=birth_date, country=country)
            #print(profile)
            profile.save()
            print("Created user " + str(i))

    def create_random_user(self, email_from_profile_object):
        import csv
        from users.models import CustomUser as User
        from profile.models import Profile
        import random

        username = random.choice(self.usernames)
        self.usernames.remove(username)

        password = User.objects.make_random_password()
        #Make sure that the profile object and user it is tied to have the same email
        user = User.objects.create_user(username, email_from_profile_object, password)
        return user
    
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
           
            # or can just run  UPDATE profile_table SET user_id = NULL; then DELETE FROM auth_user WHERE is_superuser IS FALSE;
            for row in cursor.fetchall():
                """
                    delete the one-to-one relationship

                    ERROR:  update or delete on table "auth_user" violates foreign key constraint "profile_table_user_id_fd445281_fk_auth_user_id" on table "profile_table"
                    DETAIL:  Key (id)=(33044) is still referenced from table "profile_table".

                """
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

    def print_all_users(self):
        from django.db import connection 

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM "auth_user";""")           

            for row in cursor.fetchall():
                print(row)

    def delete_all_users_and_profiles(self):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("UPDATE profile_table SET user_id = NULL")
            cursor.execute("DELETE FROM auth_user WHERE is_superuser is FALSE")
            cursor.execute("DELETE FROM profile_table")


            

fake_data = FakeData()
#fake_data.delete_all_users_except_admins()
#fake_data.delete_all_users_and_profiles()
start_time = time.time()
fake_data.insert_mock_data()
print('It took {0:0.1f} seconds'.format(time.time() - start_time))
print("Finished")
#fake_data.print_all_users()


