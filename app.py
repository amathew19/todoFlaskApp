from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
import config

app = Flask(__name__)

client = MongoClient('localhost', 27017, username=config.dbUser, password=config.dbPassword)
db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
