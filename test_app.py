import requests

def test_get_tasks():
    response = requests.get("http://localhost:5000/tasks")
    assert response.status_code == 200

def test_create_task():
    new_task = {"title": "Test Task"}
    response = requests.post("http://localhost:5000/tasks/create", json=new_task)
    assert response.status_code == 201  


#failing, just for testing
def test_home_failing():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is not expected message"}
    
def test_home():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my Flask app!"}
 