import psycopg2

DB_PARAMS = {
    'dbname': 'Library',
    'user': 'postgres',
    'password': 'dbms0907*',
    'host': 'localhost',
    'port': '5432'
}

def connect_to_db():
    return psycopg2.connect(**DB_PARAMS)
