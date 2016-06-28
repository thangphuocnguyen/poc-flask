#!/bin/bash
PORT=$1

echo "--------------------------------------------------------------------------------"
echo "Run Django Development Server"
echo "--------------------------------------------------------------------------------"

# Gets the current timestamp

PORT=$1

if [ "$PORT" = "" ]; then
    PORT='8000'
fi
sudo kill -9 $(sudo lsof -t -i:8000)

$APP_ENV_DIR/bin/python $BACKEND_DIR/manage.py runserver 0.0.0.0:$PORT
