from flask import Flask, render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

app = Flask(__name__)
app.secret_key = 'adasSADAASD1231231sada123'

def db_connection():
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='admin',
        database='test_123'
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, username, password FROM users WHERE username = %s', (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            print(f'User {user[1]} successfully logged in.')
            return redirect(url_for('user_page'))
        else:
            print('Something went wrong')
            return render_template('index.html')

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not username or not password or not confirm_password:
            print('All field is requared')
            return render_template('register.html')

        if password != confirm_password:
            print('Password does not match')
            return render_template('register.html')

        hashed_password = generate_password_hash(password)
        conn = db_connection()
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
            conn.commit()
            print('Username registered')
            return redirect(url_for('index'))
        except psycopg2.IntegrityError:
            conn.rollback()
            print('Username exists')
            return render_template('register.html')
        except Exception as e:
            conn.rollback()
            print(f'Error with {e}')
            return render_template('register.html')
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    return render_template('register.html')

@app.route('/user_page')
def user_page():

    if 'username' in session:

        return render_template('user_page.html', username=session['username'])
    else:
        print('Access denied: You are not logged in.')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    print('User logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)