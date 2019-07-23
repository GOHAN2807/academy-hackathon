import os

from flask import (Flask, request, render_template)

#fake DB
todo_store = {}
todo_store['utkarsh'] = ['Go for run','listen Rock Music','jogg']
todo_store['dwij'] = ['Go for run','listen Rock Music','jogg']
todo_store['mishra'] = ['Go for run','listen Rock Music','jogg']
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        global todo_store
        return todo_store[name]

    def insert_todos(name, todo):
        global todo_store
        current_todos = todo_store.get(name,[])
        current_todos.append(todo)
        todo_store[name] = current_todos
        

    def add_todo_by_name(name, todo):
        # call DB function
        if name!=None and todo!=None:
            insert_todos(name,todo)
        return

    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None
    
    #http://127.0.0.1:5000/todos?name=abcd
    @app.route('/todos')
    def todos():
        name = request.args.get('name')


        person_todos_list = get_todos_by_name(name)
        if person_todos_list == None:
            return render_template('404.html'), 404
        else:
            return render_template('todo_view.html',todos=person_todos_list)
    
    # a simple page that list my todos
    
    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name,todo)
        return "Added Successfully"

    
    @app.route('/')
    def home():
        return "Yaha kyu aya hai be"
    return app

