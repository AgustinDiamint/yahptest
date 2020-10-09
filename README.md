# Yahp
## Requirements
1. MySQL
2. Python
3. Django
4. mysql-to-python-connector

## Steps to run
Change the database name, user and password in the yahptest/settings.py file to match the local database information. 

Run from the root folder:

`python manage.py makemigrations checkusers`
`python manage.py migrate`

To create the appropriate tables in the database.

Then run `python updater.py` to populate the database with information from the api

Finally run `python manage.py runserver` to execute the application and access it at
`http://127.0.0.1:8000/




