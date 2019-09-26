### Running python from the virtual environment in Visual Studio Code

django-admin startproject VRWareWebApp
python manage.py startapp api
python manage.py startapp frontend



When running the server, if python says that the socket is already in use, use the following command to find the port number python is running on and use kill -9 port_number: netstat -ntlp

python manage.py makemigrations api
python manage.py migrate 

python manage.py makemigrations api - adds 0001_initial.py) to migrations folder. python manage.py sqlmigrate api 0001 to view SQL statements for specific migration of the app. 

Create a new user on the command line: python manage.py createsuperuser