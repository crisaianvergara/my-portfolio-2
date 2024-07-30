# Django Setup

# Create the project directory
mkdir <directory_name>
cd <directory_name>

# Create a virtual environment to isolate our package dependencies locally
python -m venv .venv - create a virtual environment
source .venv/Scripts/activate - activate environment
deactivate - deactivate environment

# Requirements
touch requirements.txt - create a requirements.txt file
pip freeze > requirements.txt - record all installed modules into the requirements.txt file
pip install -r requirements.txt - install dependencies from the requirements.txt file

# Install Django
python.exe -m pip install --upgrade pip - upgrade pip
python -m pip install Django - install latest the Django version
python -m django --version - check Django version

# Create project
django-admin startproject <project_name> . # Note the trailing '.' character
python manage.py reserver - run the application

# Create app
python manage.py startup <app_name> - create app same directory as the <project_name>

# Database setup
pip install "psycopg[binary]" - install psycopg

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["POSTGRES_DB"],
        'USER': os.environ["POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': os.environ["POSTGRES_HOST"],
        'PORT': os.environ["POSTGRES_PORT"],
    }
}

# Set timezone
pip install pytz - install pytz
TIME_ZONE = 'Asia/Manila' - set timezone to Asia/Manila PH

# Migration
python manage.py makemigrations - to create migrations for those changes
python manage.py migrate - to apply those changes to the database

python manage.py sqlmigrate project 0001 - takes migration names and returns their SQL
python manage.py check - checks for any problems in your project without making migrations or touching the database

# Django Shell
python manage.py shell - open Django shell

# Creating an admin user
python manage.py createsuperuser
Username: <username>
Email address: <email_address>
Password: <password>

# Static Files
pip install whitenoise - install whitenoise
python manage.py collectstatic

# Dot Env
pip3 install python-dotenv - install dotenv

# Gunicorn
pip3 install gunicorn