from flask import Flask,request,jsonify

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/todos', methods=['GET'])
def get_todos():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    
    todos.pop(position)
    return jsonify(todos), 200


# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)