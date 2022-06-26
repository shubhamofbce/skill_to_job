# skill_to_job

Steps to setup the project
1. Install Postgresql in your local system
2. Create a database with name skilljob in your database.
3. Note down your db credentials like DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
4. Create a .env file in the root directory and fill your credentials in env file.

```
DEBUG=True
SECRET_KEY=ask-secret-key-from-maintainer
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
AWS_ACCESS_KEY=key
AWS_SECRET_KEY=secret
```
5. Create a new venv and activate your virtual environment
6. Install all the requirements 
``pip install -r requirements.txt``
7. After this run migration
``./manage.py migrate``
8. Create a super user in your local to access admin panel
`` ./manage.py createsuperuser``
9. Run the app using ``./manage.py runserver``