# myth-caster-api

This is the backend for the MythCaster project, which aims to be a repository of characters & NPCs for Dungeons and Dragons 5e, using the SRD content as well as homebrew.

It is built using Python, specifically Django with Django Rest Framework, and uses a Postgres Database.

## Contributing

### Prerequisistes for Local development

- Docker and Docker-Compose installed
- a `mythcaster.env` file, which should define:
  - DJANGO_SECRET_KEY: can be pulled from a default django quickstart project
  - POSTGRES_DB: Name of the database to use.
  - POSTGRES_USER: User account to access postgres with
  - POSTGRES_PASSWORD: Password of user to access postgres with
  - POSTGRES_HOST: Host IP Address/Domain Name where the postgres database is hosted

### Set up a virtualenv for the project

Make sure you set up a virtualenv for the project, to help manage the `requirements.txt` file.

Once you have a virtual environment set up for python, you can install the dependencies:

```bash
pip install -r requirements.txt
```

### Running a local server

1. Make sure you run the database: `docker-compose up -d postgres`
1. Run the python container: `docker-compose up django`
1. Start coding! Changes will automatically refresh the code, and errors will log to your terminal.

### Running & creating database migrations

If any of your changes require migrations to be created, any migrations not requiring user input can be created automatically the next time the docker container spins up. Create them with:

```bash
docker-compose down
docker-compose up
```

If any migrations require user input, you will have to shell into the python container:

```bash
docker-compose run django bash
```

Once you are in, you can run the following commands to create and run migrations, and punch input into any prompts needed:

```bash
cd app
python manage.py makemigrations
python manage.py migrate
```
