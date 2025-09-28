"""
Unit tests for the Flask Task Management API
"""

import pytest
import json
from app import app, tasks


@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_task():
    """Sample task data for testing"""
    return {
        'title': 'Test Task',
        'description': 'This is a test task'
    }


class TestHealthEndpoint:
    """Test health check endpoint"""
    
    def test_health_check(self, client):
        """Test health check returns 200 and correct structure"""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'status' in data
        assert 'timestamp' in data
        assert 'version' in data
        assert data['status'] == 'healthy'


class TestTaskEndpoints:
    """Test task CRUD operations"""
    
    def setup_method(self):
        """Clear tasks before each test"""
        tasks.clear()
    
    def test_get_empty_tasks(self, client):
        """Test getting tasks when none exist"""
        response = client.get('/tasks')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['count'] == 0
        assert data['tasks'] == []
    
    def test_create_task_success(self, client, sample_task):
        """Test successful task creation"""
        response = client.post('/tasks', 
                             data=json.dumps(sample_task),
                             content_type='application/json')
        
        assert response.status_code == 201
        
        data = json.loads(response.data)
        assert 'id' in data
        assert data['title'] == sample_task['title']
        assert data['description'] == sample_task['description']
        assert data['status'] == 'pending'
        assert 'created_at' in data
        assert 'updated_at' in data
    
    def test_create_task_missing_title(self, client):
        """Test task creation without required title"""
        response = client.post('/tasks', 
                             data=json.dumps({'description': 'No title'}),
                             content_type='application/json')
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'Title is required' in data['error']
    
    def test_create_task_invalid_json(self, client):
        """Test task creation with invalid JSON"""
        response = client.post('/tasks', 
                             data='invalid json',
                             content_type='application/json')
        
        assert response.status_code == 500
    
    def test_get_task_success(self, client, sample_task):
        """Test getting a specific task"""
        # First create a task
        create_response = client.post('/tasks', 
                                    data=json.dumps(sample_task),
                                    content_type='application/json')
        
        task_data = json.loads(create_response.data)
        task_id = task_data['id']
        
        # Then get it
        response = client.get(f'/tasks/{task_id}')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['id'] == task_id
        assert data['title'] == sample_task['title']
    
    def test_get_task_not_found(self, client):
        """Test getting a non-existent task"""
        response = client.get('/tasks/nonexistent-id')
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'Task not found' in data['error']
    
    def test_update_task_success(self, client, sample_task):
        """Test successful task update"""
        # Create a task first
        create_response = client.post('/tasks', 
                                    data=json.dumps(sample_task),
                                    content_type='application/json')
        
        task_data = json.loads(create_response.data)
        task_id = task_data['id']
        
        # Update the task
        update_data = {
            'title': 'Updated Task',
            'status': 'in_progress'
        }
        
        response = client.put(f'/tasks/{task_id}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['title'] == 'Updated Task'
        assert data['status'] == 'in_progress'
        assert data['description'] == sample_task['description']  # Should remain unchanged
    
    def test_update_task_not_found(self, client):
        """Test updating a non-existent task"""
        update_data = {'title': 'Updated Task'}
        
        response = client.put('/tasks/nonexistent-id',
                            data=json.dumps(update_data),
                            content_type='application/json')
        
        assert response.status_code == 404
    
    def test_delete_task_success(self, client, sample_task):
        """Test successful task deletion"""
        # Create a task first
        create_response = client.post('/tasks', 
                                    data=json.dumps(sample_task),
                                    content_type='application/json')
        
        task_data = json.loads(create_response.data)
        task_id = task_data['id']
        
        # Delete the task
        response = client.delete(f'/tasks/{task_id}')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'message' in data
        
        # Verify task is deleted
        get_response = client.get(f'/tasks/{task_id}')
        assert get_response.status_code == 404
    
    def test_delete_task_not_found(self, client):
        """Test deleting a non-existent task"""
        response = client.delete('/tasks/nonexistent-id')
        assert response.status_code == 404


class TestErrorHandlers:
    """Test error handling"""
    
    def test_404_handler(self, client):
        """Test 404 error handler"""
        response = client.get('/nonexistent-endpoint')
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'Endpoint not found' in data['error']


class TestTaskWorkflow:
    """Test complete task workflow"""
    
    def setup_method(self):
        """Clear tasks before each test"""
        tasks.clear()
    
    def test_complete_task_lifecycle(self, client):
        """Test creating, updating, and deleting a task"""
        # Create task
        task_data = {
            'title': 'Lifecycle Test Task',
            'description': 'Testing complete lifecycle'
        }
        
        create_response = client.post('/tasks', 
                                    data=json.dumps(task_data),
                                    content_type='application/json')
        
        assert create_response.status_code == 201
        created_task = json.loads(create_response.data)
        task_id = created_task['id']
        
        # Update task status
        update_response = client.put(f'/tasks/{task_id}',
                                   data=json.dumps({'status': 'completed'}),
                                   content_type='application/json')
        
        assert update_response.status_code == 200
        updated_task = json.loads(update_response.data)
        assert updated_task['status'] == 'completed'
        
        # Verify in task list
        list_response = client.get('/tasks')
        assert list_response.status_code == 200
        
        task_list = json.loads(list_response.data)
        assert task_list['count'] == 1
        assert task_list['tasks'][0]['id'] == task_id
        
        # Delete task
        delete_response = client.delete(f'/tasks/{task_id}')
        assert delete_response.status_code == 200
        
        # Verify deletion
        final_list_response = client.get('/tasks')
        final_task_list = json.loads(final_list_response.data)
        assert final_task_list['count'] == 0
