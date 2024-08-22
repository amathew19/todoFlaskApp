from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
import config

app = Flask(__name__)

client = MongoClient(username=config.dbUser, password=config.dbPassword, authSource="todoFlaskDB")
db = client['todoFlaskDB']
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('main'))

    all_todos=todos.find()
    return render_template('index.html', todos=all_todos)


if __name__ == '__main__':
    app.run()
