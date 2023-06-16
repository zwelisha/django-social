# My Social Network

## Social Network Details
### Develop a simple social network.

- Users can register and login
- Users can create posts
- All users are displayed on the home page
- When you click on a user you can see their posts

#### Pages:

- Register
- Login
- Home
- Timeline

#### Models:

- Django User
- Post (User, Timestamp, Message)

#### Frameworks;

- Django
- Bootstrap


## Getting Started

### Requirements

1. Python3
2. Pip3
3. Text editor (Recommended: VSCode or SublimeText or Atom)
4. Django 4.2.2
5. Django Jquery
6. Django bootstrap 5



### Installation

#### 1. Python3

The installation differs from one operating system to the other, but the documentation which can be found [here](https://www.python.org/downloads/) have clear instructions for each operating system.

#### 2. Pip3

Pip3 is distributed with latest Python versions - which means when you download Python3 you automatically get Pip3 installed on your machine.

#### 3. Text Editor
Any text editor of your choice can be used. However Visual Studio Code and Atom are highly recommended.

#### 4. Black
Run ```pip3 install black```

#### 5. Project specific software
after cloning the project cd into the root folder and run the following commands

Run ```pip3 install -r requirements.txt```



#### Folder Structure

There are two folders for this project: `auth_app` and `mytwitter`. The folder contains all the files needed for registration and handling login. Secondly 

```
auth_app
    migrations
    static
        images
        js
    templates
        auth_app
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py

mytwitter
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgy.py
.gitignore
db.sqlite3
manage.py
README.md
requirements.txt
```

### Formatting The Code

Use Black for consistency, it takes away the pain of memorising all the PEP8 coding standards and rules.
#### formatting a file example
Run ```black filename.extension``` for example ```black main.py``` will format the main script.


### Running The Project

#### 1. Go to the root folder and run the following commands
```
python manage.py createsuperuser 
```

#### 2. Launch the app and go to the admin page to start adding users and create your test data.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then navigate to the admin panel ```your default url/admin``` and start creating test data.

#### Lastly I recommed creating a virtual environment before setting 
For details please see [Python VENV](https://docs.python.org/3/library/venv.html)

#### Authors

[Zweli Mthethwa](https://www.linkedin.com/in/zweli-mthethwa-244b45a8/)