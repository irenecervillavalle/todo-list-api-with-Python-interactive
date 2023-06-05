from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


todos=[{ "label": "My first task", "done": False ,
"diccionario" : "My second task", "done": False}]

@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'hello world'


@app.route('/todos', methods=['GET'])
def hello():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    json_text = jsonify(todos)
    return json_text

# Estas dos líneas siempre seben estar al final de tu archivo app.py.

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)