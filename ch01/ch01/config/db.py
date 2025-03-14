# from __main__ import app
import psycopg2
import functools
from os import environ  # requires installing the python-dotenv


def connect_db(func):
    @functools.wraps(func)
    def repo_function(*args, **kwargs):
        # Establish the DB connection
        conn = psycopg2.connect(
            # host=app.config['DB_HOST'],
            host=environ.get('DB_HOST'),
            # database=app.config['DB_NAME'],
            database=environ.get('DB_NAME'),
            # port=app.config['DB_PORT'],
            port=environ.get('DB_PORT'),
            # user=app.config['DB_USER'],
            user=environ.get('DB_USER'),
            # password=app.config['DB_PASS'])
            password=environ.get('DB_PASS')
            )

        # Pass the connection to the wrapped function
        resp = func(conn, *args, **kwargs)

        # Commit the CRUD transaction
        conn.commit()
        conn.close()
        return resp
    return repo_function
