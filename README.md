#### Fitness App

A simple Training Log for simple workouts

#### Running the server

Requirements:
1. pipenv or pip3 to install python dependencies seen in ```Pipfile```
2. Postgresql with a database named ```fitness```
3. Fill in a secret key to ```env.example``` then rename to ```.env```

Getting Started:
1. Assuming postgres is installed and you have a user, ```createdb fitness```
2. ```pipenv install``` to install requirements to virtual environment
3. ```pipenv run python manage.py migrate``` to run migrations
4. ```pipenv run python manage.py runserver``` to run the server (default localhost:8000)

#### Project Quickstart
* Fitness holds project based settings and functionality
* Lifting is and app that holds models to Lifting
    * ```lifting/models.py``` is where you see the models that get created inside Postgres
    * ```lifting/serializers.py``` is where you see the models get serialized to and fro python and json
    * ```lifting/views.py``` is where you see the models create GET, POST, PUT, PATCH, DELETE functionality
    * ```lifting/urls.py``` is where the views get the specific endpoints created