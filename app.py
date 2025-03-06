from flask import Flask, jsonify, request


app = Flask(__name__)

# Simple in-memory data store
tasks = [
    {"id": 1, "title": "Task 1"},
    {"id": 2, "title": "Task 2"}
]


# Define a route for the root URL
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to my Flask app!"})
    
    
# Define routes for tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/create', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json['title']
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


# Run the app
#host="0.0.0.0" tells Flask to listen on all available network interfaces.
#This allows your app to be accessible from outside the container.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
