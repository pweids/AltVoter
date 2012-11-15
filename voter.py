import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/voter.db'
DEBUG = True
SECRET_KEY = None
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
    
@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('new_vote')
def add_vote():
    
    
if __name__ == '__main__':
    app.run()