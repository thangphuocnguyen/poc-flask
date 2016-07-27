## Prerequisites:
+ [Docker](https://docs.docker.com/engine/installation/)
	> Docker is an open platform for developing, shipping, and running applications.
	
+ [Docker Machine](https://docs.docker.com/machine/install-machine/) 
	
	> (For Mac/Windows)
	
	> Docker Machine is a tool that lets you install Docker Engine on virtual hosts, and manage the hosts with docker-machine commands.
	
+ [Docker Compose](https://docs.docker.com/compose/install/)
	
	> Compose is a tool for defining and running multi-container Docker applications.

*Notes: On case of using Mac/Windows, just only install [docker-toolbox](https://docs.docker.com/toolbox/overview/) to have all of three (Docker, Docker Compose, Docker Machine)*

## Getting up and run:

+ Clone the docker-django to your machine:

	```
	$ git clone git@gitlab.asoft-python.com:g-thangnguyen/python-training.git
	
	$ cd docker-django
	
	```
	
+ Create the Machine (Optional)

	```
	$ docker-machine create --driver virtualbox dev
	
	# Active machine
	$ eval $(docker-machine env dev)
	
	```

+ Build all composes & boot the system

	```
	$ docker-compose -f docker-compose-dev.yml build
	
	$ docker-compose -f docker-compose-dev.yml up

	```
