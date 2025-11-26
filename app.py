from flask import Flask, jsonify, request 
 
app = Flask(__name__) 
 
data = [ 
    {"id": 1, "name": "Prathamesh"},
    {"id": 2, "name": "Jaid"},
    {"id": 3, "name": "Rahul"},
    {"id": 4, "name": "Siddharth"},
    {"id": 5, "name": "Shital"},
] 
 
@app.route('/') 
def home(): 
    return "Cloud API Home"

@app.route('/users', methods=['GET']) 
def get_users(): 
    return jsonify(data) 
 
@app.route('/users', methods=['POST']) 
def add_user(): 
    new_user = request.json 
    data.append(new_user) 
    return jsonify(new_user), 201 
 
@app.route('/users/<int:user_id>', methods=['GET']) 
def get_user(user_id): 
    user = next((u for u in data if u["id"] == user_id), None) 
    if user: 
        return jsonify(user) 
    return jsonify({"error": "User not found"}), 404 
 
if __name__ == "__main__": 
    app.run(debug=True, port=8080)