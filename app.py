from flask import Flask
from pymongo import MongoClient
import config

app = Flask(__name__)

client = MongoClient('localhost', 27017, username=config.dbUser, password=config.dbPassword)


db = client.flask_db
todos = db.todos

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
