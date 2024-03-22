# import pytest
# from app import create_app, db
# from app.models import Task
# from config import TestConfig


# @pytest.fixture
# def client():
#     app = create_app(TestConfig)
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()
#         yield client
#         with app.app_context():
#             db.session.remove()
#             db.drop_all()

# def test_create_task(client):
#     response = client.post('/tasks', json={
#         'name': 'Test Task',
#         'due_date': '2023-01-01',
#         'priority': 1,
#         'status': 0
#     })
#     assert response.status_code == 201
#     assert response.json['id'] == 1

# def test_get_tasks(client):
#     response = client.get('/tasks')
#     assert response.status_code == 200
#     assert isinstance(response.json, list)

# # Add more tests for update and delete operations

