import pytest
from app import create_app, db
from app.models.tasks_model import Task
from datetime import date

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
    Task.query.delete()
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
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['name'] == 'Buy apples'
    assert response.json[1]['name'] == 'Buy pears'
