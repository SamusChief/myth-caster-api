# myth-caster-api

This is the backend for the MythCaster project, which aims to be a repository of characters & NPCs for Dungeons and Dragons 5e, using the SRD content as well as homebrew.

It is built using Python, specifically Django with Django Rest Framework, and uses a Postgres Database.

## Contributing

### Prerequisistes for Local development

- Docker and Docker-Compose installed
- a `mythcaster.env` file, an example is provided below

```env
# Docker settings
# DOCKER_PYTHON_TAG=3  # optional; default is 3
# DOCKER_DJANGO_CONTAINER_NAME=myth-caster-django  # optional; default is myth-caster-django
# DOCKER_POSTGRES_TAG=12  # optional; default is 12
# DOCKER_POSTGRES_CONTAINER_NAME=myth-caster-postgres  # optional; default is myth-caster-postgres
# DOCKER_POSTGRES_DATA_DIR=/data/postgres/myth-caster-api  # optional; default is /data/postgres/myth-caster-api

# Django Settings
DJANGO_SECRET_KEY='h=cwo7sd1%s!h!3jy3g72j3#l-s=s-21gfng!=!vwv56rqyng!'  # required; generate using https://miniwebtool.com/django-secret-key-generator/

# Database Settings
POSTGRES_DB=mythcaster  # required; identifies the database used by the app
POSTGRES_USER=mythcaster  # required; identifies the user, who should have access to the above DB
POSTGRES_PASSWORD=supersecretpassword  # required; you should change this
POSTGRES_HOST=postgres  # required; used to connect to postgres instance
# POSTGRES_PORT=5432  # optional; default is 5432

# Logging settings
# LOG_LEVEL=WARN  # optional; default is WARN

```

### Running a local server

1. Make sure you run the database: `docker-compose up -d postgres`
1. Run the python container: `docker-compose up django`
1. Start coding! Changes will automatically refresh the code, and errors will log to your terminal.
1. If you need to run a `manage.py` script, you can use the `-d` flag to run the django service as well. Then, you can follow the instructions below in `Running & creating database migrations`.

#### Rebuilding the Django service

The Django container runs in its own built docker container, defined by the `Dockerfile` in the project root. Whenever you change this file or the project's `requirements.txt` file, you will need to rebuild this container. To do so, on next startup, run this instead:

```bash
docker-compose up --build django
```

### Running & creating database migrations

When you first run the application, you will need to run migrations as well. If you make changes to a model, or add one, you will need migrations for that as well.

First, run the django service in a detached state:

```bash
docker-compose up -d django
```

#### Creating Migrations

To create migrations, run the following script:

```bash
docker-compose exec django python manage.py makemigrations
```

#### Running migrations

To run migrations, run the following script:

```bash
docker-compose exec django python manage.py migrate
```

#### Other manage.py scripts

You can run other manage.py scripts, such as `test`, `createsuperuser`, and any custom scripts by following the same format as above. Alternatively, you can shell into the containers, and run the scripts directly.

When using `startapp` to create new sections, it is recommended to do so as a non-root user outside of your docker container. Do do this, you will need a python environment.
