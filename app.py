# app.py
from flask import Flask, request, jsonify
import os
from pymongo import MongoClient

app = Flask(__name__)

mongo_host = os.getenv('MONGO_HOST', 'mongodb')
client = MongoClient(host=mongo_host, port=27017)

db = client['flask_app']

def create_users_collection():
    if 'users' not in db.list_collection_names():
        db.create_collection('users')

create_users_collection()
print('coneected to mongo!!!')
@app.route('/')
def index():
    return jsonify(message="Welcome to the Flask App!")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify(error="Name and age are required."), 400

    user = {
        "name": name,
        "age": age
    }
    db.users.insert_one(user)

    return jsonify(message="Data stored successfully.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
