#!/bin/bash

NAME="simple-django"     	                        # Name of the application
DJANGODIR=tras.simpledjango             	  	# Django project directory
SOCKFILE=/tras.simpledjango/run/gunicorn.sock  	  	# we will communicte using this unix socket
USER=vagrant                                      	# the user to run as
GROUP=webapps                                     	# the group to run as
NUM_WORKERS=3                                     	# how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.dev        	# which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi                     	# WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
echo "PWD:" $PWD
echo "DJANGODIR:" $DJANGODIR
cd $DJANGODIR
echo "PWD:" $PWD

# source .bashrc
# source venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


# # Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
echo "RUNDIR:" $RUNDIR
test -d $RUNDIR || sudo mkdir -p $RUNDIR

# # Start your Django Unicorn
# # Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn $DJANGO_WSGI_MODULE:application
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-