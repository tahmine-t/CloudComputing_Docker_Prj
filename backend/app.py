# app.py

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

db_user = os.getenv('DATABASE_USER','myuser')
db_pass = os.getenv('DATABASE_PASS','mypassword')
db_db = os.getenv('DATABASE_DB','mydatabase')
db_host = os.getenv('DATABASE_HOST','localhost')

db_conf = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_db}'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_conf
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

def init_db():
    conn = psycopg2.connect(dbname=db_db, 
                            user=db_user, password=db_pass, 
                            host=db_host)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname={db_db}")
    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE mydatabase")
        cursor.execute(f"CREATE USER myuser WITH ENCRYPTED PASSWORD {db_pass}")
        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE mydatabase TO {db_user}")
    cursor.close()
    conn.close()
    
with app.app_context():
    # init_db()
    db.create_all()

@app.route('/api')
def home():
    return "Hello, Flask!"

# Create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        result.append(user_data)
    return jsonify(result), 200

# Get a single user by ID
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    user_data = {'id': user.id, 'name': user.name, 'email': user.email}
    return jsonify(user_data), 200

# Update a user
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

# Delete a user
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
