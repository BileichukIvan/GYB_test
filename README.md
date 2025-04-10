# GYB_test
This project is a simple Flask-based REST API for managing users. It supports basic CRUD operations (Create, Read, Update, Delete) for users, with data stored in a PostgreSQL database. The API is containerized using Docker and includes Swagger documentation for easy testing.

# Features
* Create a new user: ```POST /users```

* Get all users: ```GET /users```

* Get a specific user: ```GET /users/{id}```

* Update a user: ```PUT /users/{id}```

* Delete a user: ```DELETE /users/{id}```

Each user has the following fields:

* ```id``` (integer, primary key)

* ```name``` (string)

* ```email``` (string, unique)

* ```created_at``` (datetime, auto-generated)

# Project structure
```aiignore
GYB_test/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── seeders.py
│   └── docs/
│       └── user_docs.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_routes.py
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── initial_migration.py
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── requirements.txt
├── run.py
├── seed.py
└── README.md
```

# Installation

1. Clone the repository:
```bash
 git clone https://https://github.com/BileichukIvan/GYB_test
 cd GYB_test
```

2. Setup virtual environment
```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```
3. Setup environmental variables in .env file, for example:
```aiignore
 FLASK_APP=run.py
 FLASK_ENV=development
 FLASK_DEBUG=TRUE
 DATABASE_URL=postgresql://user:password@localhost:5432/userdb
 POSTGRES_DB=userdb
 POSTGRES_USER=user
 POSTGRES_PASSWORD=password
```
4. Run your Database on selected port and start your app with:
```bash
 pipenv run flask db upgrade
 pipenv run flask run
```
Or use Docker to run this project:
```bash
 docker-compose up --build
 docker-compose exec web flask db upgrade
```
5. Access the API:
* The API will be available at ```http://localhost:5000```.
* Swagger documentation will be available at ```http://localhost:5000/apidocs```.

6. Tests. You can run tests for api with:
```bash
 pytest tests/
```
Or in docker container:
```bash
 docker-compose exec web pytest -v tests/
```
7. DB seeding. You can also seed the DB with example data.
```bash
 pipenv run python seed.py
```
Or in docker container:
```bash
 docker-compose exec web python seed.py
```

