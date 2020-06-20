<h2 align="center">Spending Journal</h2>

### How much did I spend yesterday/ last week / last month, and what were they?

Everything in Spending Journal was designed to help answer these questions.

### For Development

#### Installation

We make use of Docker containers to create a pure-Docker development environment, which frees us from <b>directly installing dependencies</b> on our machines, as well as to easily <b>provide a common environement</b> for all the contributors. With that being said, [Docker Compose](https://docs.docker.com/compose/) is the correct tool for this purpose.

The idea is to mount the source code of each module - api and web - into a corresponding container.

> NOTE: The following installation instructions have only been tested on Linux Mint 19.3 Tricia. However, they should be applicable to other Debian-based distros as well.

1. Build images and create containers with the docker-compose command.
```console
docker-compose --file docker-compose.development.yml up -d
```
2. At this time, there are no tables in the database and we need to manually instruct the API service to generate the tables.
```console
docker exec -it api flask shell
# Inside the flask shell
from main import db
db.create_all()
``` 
3. You can now open your browser at the localhost address to have a look. However, we're integrating Google Sign-In into our web application and it requires a valid domain name to work. So you need to map your loopback IP address to *spendingjournal.com* in the /etc/hosts file.
