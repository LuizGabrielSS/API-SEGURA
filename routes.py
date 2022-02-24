import hashlib
import datetime
from app import app
from flask import jsonify,request
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity
import hashlib

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

@app.route('/login', methods=['POST'])
def login():
    experies = datetime.timedelta(minutes=30)
    email = request.json.get('email', None)
    password = request.json.get('senha', None)
    if not email:
        return jsonify({'msg': 'Sem email!'}), 400
    if not senha:
        return jsonify({'msg': 'Senha não encontrada!'}), 400
    if email != 'teste.testando@gmail.com':
        return jsonify({'msg': 'User Not Found!'}), 404
    elif email == 'teste.testando@gmail.com':
        senha = encrypt_string(password)
        if senha != '688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6':
            return jsonify({'msg': 'Senha incorreta!'}), 404
        elif senha == '688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6':
            access_token = create_access_token(email,expires_delta=experies)
            return {"access_token": access_token}, 200

# protected test route
@app.route('/test', methods=['GET'])
@jwt_required
def test():
    user = get_jwt_identity()
    email = user['email']
    return f'Welcome to the protected route {email}!', 200
