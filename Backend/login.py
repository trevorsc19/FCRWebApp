from django.contrib.auth import authenticate, login

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    print("Username: {} password: {}".format(username, password))
    
    return "user: {} first_name: {} last_name: {} email: {} birth_date: {} country: {}".format(self.user.get_username(),self.first_name, self.last_name, self.email, self.birth_date, self.country)
