from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/users")
def get_users():
    return "Não há usuários"

if __name__ == "__main__":
    app.run(debug=True)