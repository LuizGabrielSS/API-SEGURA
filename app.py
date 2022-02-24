from flask import Flask,jsonify,request
from routes import *
from flask_jwt_extended import JWTManager

app = Flask(__name__)
with open('confidencial/senha', 'r', encoding='utf-8') as banco :
    senha=banco.read()

app.config["JWT_SECRET_KEY"] = senha

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)