from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)

# Modelo de Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

db.create_all()

# Rutas para interactuar con la base de datos
@app.route('/producto', methods=['POST'])
def crear_producto():
    try:
        data = request.get_json()
        nuevo_producto = Producto(nombre=data['nombre'], precio=data['precio'])
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({"mensaje": "Producto creado", "id": nuevo_producto.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/producto/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    try:
        producto = Producto.query.get_or_404(producto_id)
        producto_dict = deepcopy({"nombre": producto.nombre, "precio": producto.precio})
        return jsonify(producto_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
