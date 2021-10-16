# django-login-register-crud

portfolio project with django. Just login if you have a account, register if you don't. crud your profile info.

# requirements

postgresql 13
python3.9.6
requirement/development.pip

## developer

This section explains how to develop the system.

Make sure you have python == 3.9.6 installed and set as enviroment variable.
if you don't know how to do this yo can check ( [Python 3.9 documentation](https://docs.python.org/3.9/) )

First things first you should clone our repo to your local machine for development purposes.

open a folder that you want to have project in and open terminal and write:

```bash
git clone https://github.com/bhdrkcr/awesomeinventory.git
```

After that you should create a virtual enviroment

if you don't know how enviroments function I suggest you to [read documentation](https://docs.python.org/3/library/venv.html)

```bash
cd InovationPortal
python3 venv env
```

activate your enviroment

```bash
source env/bin/activate
```

now you have to install needed required libraries.
since we want to get development requirements, you can do this by:

```bash
pip install -r requirements/development.pip
```

Now you can export your environment variables
we are using python decouple so you can create a .env file in main dir and type in your variables:

```bash
PYTHONPATH=<main-dir-name-youve-given>

SECRET_KEY=<secret key>

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=
DEFAULT_FILE_STORAGE=

ALLOWED_HOSTS= 127.0.0.1, localhost

SQL_ENGINE=<database engine>
SQL_DATABASE=<database name>
SQL_USER=<database user>
SQL_PASSWORD=<database password>
SQL_HOST=<database host>
SQL_PORT=<database port>
```

after that you can migrate and ready to rock n roll

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

### Notes for developer

- Use djangos coding style [django coding style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- Name your Classes based on classes their inherited.
  - for example if you want to name a view class name it like `VehicleAddFormView(FormView):` so when you inherit in urls you will know that is a formview.
- never push your new page commits (like new url-page-model-template) without testing and documenting.
- Push your fixes after you test and update the document. Commit names should explain the fix.
- Name your commits accordingly.
