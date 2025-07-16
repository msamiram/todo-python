from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models.task import Task
from utils.helpers import get_current_user

task_bp = Blueprint('task', __name__)
VALID_STATUSES = ['New', 'In Progress', 'Completed']

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user = get_current_user()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status = request.args.get('status')

    query = Task.query.filter_by(user_id=user.id)
    if status:
        query = query.filter_by(status=status)

    tasks = query.paginate(page=page, per_page=per_page)
    return jsonify({
        'tasks': [task.to_dict() for task in tasks.items],
        'total': tasks.total,
        'pages': tasks.pages,
        'current_page': tasks.page
    }), 200


@task_bp.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def task_operations(task_id):
    user = get_current_user()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    if request.method == 'GET':
        return jsonify(task.to_dict()), 200

    if request.method == 'PUT':
        data = request.get_json()
        if 'status' in data and data['status'] not in VALID_STATUSES:
            return jsonify({'error': 'Invalid status'}), 400

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        db.session.commit()
        return jsonify(task.to_dict()), 200

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200


@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user = get_current_user()
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    status = data.get('status', 'New')
    if status not in VALID_STATUSES:
        return jsonify({'error': 'Invalid status'}), 400

    task = Task(
        title=data['title'],
        description=data.get('description'),
        status=status,
        user_id=user.id
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@task_bp.route('/tasks/<int:task_id>/progress', methods=['PUT'])
@jwt_required()
def progress_task(task_id):
    user = get_current_user()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.status = 'In Progress'
    db.session.commit()
    return jsonify(task.to_dict()), 200



@task_bp.route('/tasks/<int:task_id>/complete', methods=['PUT'])
@jwt_required()
def complete_task(task_id):
    user = get_current_user()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.status = 'Completed'
    db.session.commit()
    return jsonify(task.to_dict()), 200
