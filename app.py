from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        # Insert user data into the SQLite database
        c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        return redirect(url_for('welcome'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
