This is training repo for Python
Author: Thang Nguyen
Email: thang.nguyenphuoc@asnet.co.vn

# Django training - notes

> sudo apt-get update


## Install pyenv
<https://github.com/yyuu/pyenv>
<https://gist.github.com/softwaredoug/a871647f53a0810c55ac>
<http://opencafe.readthedocs.io/en/latest/getting_started/pyenv/>

> sudo apt-get install git python-pip make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

> sudo pip install virtualenvwrapper

> git clone https://github.com/yyuu/pyenv.git ~/.pyenv
> git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

> echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

> echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

> echo 'eval "$(pyenv init -)"' >> ~/.bashrc

> echo 'pyenv virtualenvwrapper' >> ~/.bashrc

> exec $SHELL

// Check version
> pyenv --version

## Installing a fresh version of Python (via pyenv)

// Install
> pyenv install 3.4.2

// Set 2.7.6 as your shell default
> pyenv global 3.4.2

// Point a project at 3.4.2
// Place a hidden file .python-version in your project. In this file simply place the text: 3.4.2 into it
> touch .python-version

> vim .python-version

// bootstrap a virtual environment in this directory
> pyvenv venv

> source venv/bin/activate

// Output installed packages in requirements format.
> pip install requests
>
> pip freeze > requirements.txt


## Install Django

// Django 1.9.6
> pip install Django==1.9.6

// Check django path
> python -c "import django; print(django.__path__)"

// Check django version
> python -m django --version

> django-admin --version

> python -c "import django; print(django.get_version())"


## Create the PostgreSQL Database and User

<https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04>

> sudo apt-get update

> sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

// Install psycopg2 - Python-PostgreSQL Database Adapter
> pip install psycopg2

// Create the PostgreSQL Database and User
> sudo su - postgres

// Access PostgreSQL interactive session
> psql

// Create a database for project:
> CREATE DATABASE myproject;

// create a database user for project
> CREATE USER myprojectuser WITH PASSWORD 'password';

// Allow user access to administer new database:
> GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

// exit out of the PostgreSQL prompt
> \q

// exit out of the postgres user's shell session
> exit


## Start project (by pass from source)

> django-admin startproject djstarter

> python manage.py startapp polls

> python manage.py startapp blog


## Create superuser
// Create an administrative user for the project
> python manage.py createsuperuser

> (admin/123abc456)


## Handle models

// Telling Django that you’ve made some changes to your models
> python manage.py makemigrations polls

// See what SQL that migration would run.
> python manage.py sqlmigrate polls 0001

// Checks for any problems in your project without making migrations or touching the database.
> python manage.py check

// Migrate the db
> python manage.py migrate

// Test model from test.py specs
> python manage.py test polls


## Run server
> python manage.py runserver 0.0.0.0:8000


## Interactive Python shell
> python manage.py shell


## Others

// Since we are going to deal with datetimes, we will install the pytz module. This module provides timezone de nitions for Python and is required by SQLite to work with datetimes.
> pip install pytz
> pip install django-taggit==0.17.1


// Refs

<https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04>

// List db
> sudo su - postgres
>
> psql
>
> postgres=# \l

