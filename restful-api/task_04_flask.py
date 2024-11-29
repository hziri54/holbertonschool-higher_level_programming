#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    """Welcome message for the API"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """Return a list of all usernames"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Return a simple 'OK' message"""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Return the full object for the provided username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    data = request.get_json()

    # Check if username is provided
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Add the new user to the dictionary
    users[data["username"]] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
