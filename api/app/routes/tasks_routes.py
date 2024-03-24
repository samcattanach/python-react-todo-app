# task API routes
from flask import Blueprint, request, jsonify
from app import db
from app.models.tasks_model import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
def hello_world():
    print('Hello')
    return 'Hello'

@tasks_bp.route('/tasks')
def get_tasks():
    print('getting tasks...')
    tasks = Task.query.all()
    print("API response:", tasks)
    tasks_list = [
        {
            'id': task.id,
            'name': task.name,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'priority': task.priority,
            'status': task.status
        } for task in tasks
    ]
    print("returning:", tasks_list)
    return jsonify(tasks_list)
