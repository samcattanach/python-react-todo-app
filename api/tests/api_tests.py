import pytest
from app import create_app, db
from app.models.tasks_model import Task
from datetime import date
from sqlalchemy import text


@pytest.fixture(scope='function')
def test_client():
    flask_app = create_app()
    

    # test client for the app
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='function')
def init_database(test_client):
    print("init database...")
    # Create the database and table
    db.create_all()

    # Clear table data
    db.session.execute(text('TRUNCATE TABLE tasks RESTART IDENTITY CASCADE;'))
    db.session.commit()


    # Insert user data
    task1 = Task(name='Buy apples', due_date=date.today(), priority=0, status=3)
    task2 = Task(name='Buy pears', due_date=None, priority=3, status=0)
    db.session.add(task1)
    db.session.add(task2)
    # Commit the changes
    db.session.commit()

    # run the tests
    yield db 



def test_get_tasks(test_client, init_database):
    print("test_get_tasks...")
    response = test_client.get('/tasks')
    print(response)
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['name'] == 'Buy apples'
    assert response.json[1]['name'] == 'Buy pears'

def test_get_single_task(test_client, init_database):
    print("test_get_single_task...")
    response = test_client.get('/tasks/1')  # Assuming ID 1 exists
    print(response)
    assert response.status_code == 200
    assert response.json['name'] == 'Buy apples'
    assert response.json['priority'] == 0


def test_create_task(test_client, init_database):
    print("test_create_task...")
    new_task = {
        'name': 'Buy bananas',
        'due_date': '2024-04-18',
        'priority': 2,
        'status': 1
    }
    response = test_client.post('/tasks', json=new_task)
    print(response)
    assert response.status_code == 201
    assert response.json['id'] is not None

def test_update_task(test_client, init_database):
    print("test_update_task...")
    updates = {
        'name': 'Buy green apples',
        'priority': 1,
        'status': 2
    }
    response = test_client.put('/tasks/1', json=updates)  # Assuming ID 1 exists
    print(response)
    assert response.status_code == 200
    assert response.json['message'] == 'Task updated successfully'

    # Fetch the updated task to verify changes
    response = test_client.get('/tasks/1')
    print(response)
    assert response.json['name'] == 'Buy green apples'
    assert response.json['priority'] == 1
    assert response.json['status'] == 2

def test_delete_task(test_client, init_database):
    print("test_delete_task...")
    response = test_client.delete('/tasks/1')  # Assuming ID 1 exists
    print(response)
    assert response.status_code == 200
    assert response.json['message'] == 'Task deleted successfully'

