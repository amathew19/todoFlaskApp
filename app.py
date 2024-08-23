from flask import Flask, render_template, url_for, redirect, request
from bson.objectid import ObjectId
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
    todos_count = todos.count_documents({})

    return render_template('index.html', todos=all_todos, todos_count=todos_count)

@app.post('/<id>/delete')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()
