import hashlib
from flask import Blueprint, render_template, redirect, url_for, request
from models import User, db
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

auth_bp = Blueprint('auth', __name__)

def hash_password(password):
    password = password.encode('utf-8')
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    hashed_password = digest.finalize()
    return hashed_password.hex()


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('templates/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        user = User.query.filter_by(username=username, password=hashed_password).first()
        if user is not None:
            return redirect(url_for('main.index'))
    return render_template('templates/login.html')
