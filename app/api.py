from flask import Flask, request, Response
# from flask_sqlalchemy import
import flask_sqlalchemy
import json

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

users_data = {
    1: {
        "id": 1,
        "name": "João Bruno Rodrigues"
    },
    2: {
        "id": 2,
        "name": "Larissa Oliveira Ramos"
    },
}

def responde_users():
    return {"users": list(users_data.values())}

@app.route("/")
def root():
    return "<h1>Olá, Mundo! API com Flask</h1>"

@app.route("/users")
def list_users():
    return responde_users()

@app.route("/users", methods=["POST"])
def create_user():
    body = request.json

    ids = list(users_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    users_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }

    return responde_users()

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    user = users_data.get(user_id)

    if user:
        del users_data[user_id]

    return responde_users()

@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")
    
    if user_id in users_data:
        users_data[user_id]["name"] = name
    
    return responde_users()

app.run(debug=True)