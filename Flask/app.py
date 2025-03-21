from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)

# Agregue su solución aquí


if __name__ == '__main__':
    app.run(debug=True)
