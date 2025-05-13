from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database of users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    # Ensure that the response is an empty list if no users are present
    return jsonify([user for user in users.keys()]) if users else jsonify([])

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Check if the username is provided
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Add the user to the in-memory dictionary
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
