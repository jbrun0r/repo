from app import app
from flask import Flask

@app.route('/', methods=['GET'])
def root():
    return jsonify