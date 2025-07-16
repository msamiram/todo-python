from flask import Blueprint, send_from_directory, jsonify
import os

static_bp = Blueprint('static', __name__)

@static_bp.route('/')
def index():
    return send_from_directory('front', 'index.html')

@static_bp.route('/app.js')
def serve_js():
    return send_from_directory('front', 'app.js')

@static_bp.route('/style.css')
def serve_css():
    return send_from_directory('front', 'style.css')

@static_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join('static'), 'favicon.ico')

@static_bp.route('/api', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Todo API",
        "endpoints": {
            "register": "POST /register",
            "login": "POST /login",
            "tasks": "GET /tasks",
            "create_task": "POST /tasks",
            "get_task": "GET /tasks/<id>",
            "update_task": "PUT /tasks/<id>",
            "delete_task": "DELETE /tasks/<id>",
            "complete_task": "PUT /tasks/<id>/complete"
        }
    })
