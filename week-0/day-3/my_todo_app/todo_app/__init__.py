import os

from flask import (Flask, request)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def todo_view(todos):
        the_view = 'List of my todos:'+'<br>'
        for todo in todos:
            the_view += ( todo +'<br>' )
        the_view += '--- List ends here ---'
        return the_view

    def get_todos_by_name(name):
        if name == 'utkarsh':
            my_todos = ['Go for run','listen Rock Music','jogg']
        elif name == 'dwij':
            my_todos = ['Go for run','listen Rock Music','jogg']
        elif name =='mishra':
            my_todos = ['Go for run','listen Rock Music','jogg']
        else:
            my_todos = []
        return my_todos
        
    
    #http://127.0.0.1:5000/todos?name=abcd
    @app.route('/todos')
    def todos():
        name = request.args.get('name')

        person_todos_list = get_todos_by_name(name)
        return todo_view(person_todos_list)
    
    # a simple page that list my todos
    @app.route('/')
    def home():
        return "Yaha kyu aya hai be"
    return app

