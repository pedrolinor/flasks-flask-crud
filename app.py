from flask import Flask, request, jasonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_controller = 1
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_controller
    data = request.get_json()
    new_task = Task(id=task_id_controller, tittle=data.get('title'), description=data.get('description'))
    task_id_controller += 1
    tasks.append(new_task)
    return jasonify({"message: Tarefa craida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)