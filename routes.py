from flask import Blueprint, render_template, request
from app import mysql

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    score = request.form['score']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO results (name, score) VALUES (%s, %s)", (name, score))
    mysql.connection.commit()
    cur.close()
    return "Submitted!"