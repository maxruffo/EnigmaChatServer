import hashlib
from flask import Blueprint, jsonify, request
from auth.models import User, db
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


auth_bp = Blueprint('auth', __name__)

def hash_password(password):
    password = password.encode('utf-8')
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    hashed_password = digest.finalize()
    return hashed_password.hex()


@auth_bp.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = hash_password(password)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'}), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = hash_password(password)
    user = User.query.filter_by(username=username, password=hashed_password).first()
    if user is not None:
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password!'}), 401
