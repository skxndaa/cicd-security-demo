"""
Simple Flask Web API for DevSecOps Demo
Provides basic CRUD operations for a task management system
"""

from flask import Flask, request, jsonify
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# In-memory storage for demo purposes
tasks = {}

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API information"""
    return jsonify({
        'message': 'Welcome to DevSecOps Task Management API',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health',
            'tasks': '/tasks',
            'documentation': 'https://github.com/skxndaa/cicd-security-demo'
        },
        'status': 'running'
    }), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    }), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    logger.info("Fetching all tasks")
    return jsonify({
        'tasks': list(tasks.values()),
        'count': len(tasks)
    }), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        
        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        
        task_id = str(uuid.uuid4())
        task = {
            'id': task_id,
            'title': data['title'],
            'description': data.get('description', ''),
            'status': 'pending',
            'created_at': datetime.utcnow().isoformat(),
            'updated_at': datetime.utcnow().isoformat()
        }
        
        tasks[task_id] = task
        logger.info(f"Created task: {task_id}")
        
        return jsonify(task), 201
        
    except Exception as e:
        logger.error(f"Error creating task: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(tasks[task_id]), 200

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a specific task"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    try:
        data = request.get_json()
        task = tasks[task_id]
        
        # Update fields if provided
        if 'title' in data:
            task['title'] = data['title']
        if 'description' in data:
            task['description'] = data['description']
        if 'status' in data and data['status'] in ['pending', 'in_progress', 'completed']:
            task['status'] = data['status']
        
        task['updated_at'] = datetime.utcnow().isoformat()
        
        logger.info(f"Updated task: {task_id}")
        return jsonify(task), 200
        
    except Exception as e:
        logger.error(f"Error updating task: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a specific task"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    del tasks[task_id]
    logger.info(f"Deleted task: {task_id}")
    
    return jsonify({'message': 'Task deleted successfully'}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
