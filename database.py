import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_db():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='admin',
            database='postgres'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        try:
            cur.execute('CREATE DATABASE test_123;')
            print('Database test_123 created successfully')
        except psycopg2.errors.DuplicateDatabase as e:
            print(f'Error with {e}')
    except Exception as e:
        print(f'Error with {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='admin',
            database='test_123'
        )
        cur = conn.cursor()
        create_table = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        """
        cur.execute(create_table)
        conn.commit()
        print('Table created successfully')
    except Exception as e:
        print(f'Error with {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    create_db()