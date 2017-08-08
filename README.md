PyLogin
=======

# Development setup

This is a short guide for Linux/OS X based systems.

First clone the repository to somewhere on your computer:
```
git clone https://github.com/tekkom/PyLogin
```

We use Python 3.4+ during development.  
Setup a python virtualenv inside the folder. We name it `env`. (this whole step is optional, but is absolutely recommended):
```
pip install virtualenv             # If you haven't installed it yet

cd ./PyLogin
python virtualenv env -p python3   # This is different for windows
```

Activate the environment:
```
source ./env/bin/activate
```

Install all the requirements:
```
pip install -r ./requirements.txt
```

Do migrations and create the database:
```
python manage.py makemigrations    # Prepare changes if there are any, just do it for good measure.
python manage.py migrate           # Do the migrations and create the local database.
python manage.py createsuperuser   # Create a super user to login to the admin panel.
```

Run the server:
```
python manage.py runserver
```
The server will now start in development mode.
