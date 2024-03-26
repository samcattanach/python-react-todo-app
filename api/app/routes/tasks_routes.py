# task API routes
from flask import Blueprint, request, jsonify, abort
from app import db
from app.models.tasks_model import Task

tasks_bp = Blueprint('tasks', __name__)


# Create a new task
@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    print(request)
    data = request.json
    print(data)
    if not data or 'name' not in data or 'priority' not in data or 'status' not in data:
        abort(400, description="Missing task data in request.")
    try:
        new_task = Task(
            name=data['name'],
            due_date=data.get('due_date'),
            priority=data['priority'],
            status=data['status']
        )
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))
    return jsonify({'id': new_task.id}), 201


# Get all tasks
@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
    except Exception as e:
        abort(500, description=str(e))
    tasks_data = [{
        'id': task.id,
        'name': task.name,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'priority': task.priority,
        'status': task.status
    } for task in tasks]
    return jsonify(tasks_data), 200


# Get a single task by id
@tasks_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    try:
        task = Task.query.get_or_404(id)
    except Exception as e:
        abort(500, description=str(e))
    task_data = {
        'id': task.id,
        'name': task.name,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'priority': task.priority,
        'status': task.status
    }
    return jsonify(task_data), 200


# Update a task
@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    print(data)
    if not data:
        abort(400, description="No update data provided.")
    try:
        task.name = data.get('name', task.name)
        task.due_date = data.get('due_date', task.due_date)
        task.priority = data.get('priority', task.priority)
        task.status = data.get('status', task.status)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))
    return jsonify({'message': 'Task updated successfully'}), 200


# Delete a task
@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))
    return jsonify({'message': 'Task deleted successfully'}), 200
