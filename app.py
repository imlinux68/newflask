from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import mysql.connector


app = Flask(__name__)
Bootstrap(app)

### DB CONFIG ###


connection = mysql.connector.connect(
    user='root', 
    password='root', 
    host='mysql', 
    port="3306",
    database='my_database')
print("DB connected")

mycursor = connection.cursor()
mycursor.execute('CREATE TABLE IF NOT EXISTS user (user_name VARCHAR(30));')

@app.route('/')
def index():
    mycursor.execute("INSERT INTO user VALUES(%s)", (['John']))
    connection.commit()
    return render_template('index.html')


@app.route('/redirect')
def redire():
    return redirect(url_for('about'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/css')
def css():
    return render_template('css.html')


@app.route('/price')
def price():
    return render_template('price.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
