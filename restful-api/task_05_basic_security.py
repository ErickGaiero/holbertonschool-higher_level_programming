from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unauthorized Access (Basic Auth)"}), 401

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"error": "Missing or Invalid Token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return jsonify({"error": "Invalid Token Format"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": f"Access Granted for user: {auth.current_user()}"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[username]
    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 403

    token = create_access_token(identity=username)
    return jsonify({"access": token}), 200

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify({"message": "Access granted with JWT"}), 200

@app.route("/admin-only")
@jwt_required()
def admin_only():
    return jsonify({"message": "Admin Access: Granted (Requires valid JWT)"}), 200

if __name__ == "__main__":
    app.run(debug=True)
