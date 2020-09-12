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

Make sure you set up a virtualenv for the project, to help manage requirements.txt

### Running a local server

1. Make sure you run the database and other containers: `docker-compose up -d`
2. Run the server: `python manage.py runserver`
3. Start coding!
