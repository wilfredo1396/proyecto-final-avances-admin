from utils.db import db 

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, nullable=False)
    proveedor = db.Column(db.String(80), nullable=False)
    producto = db.Column(db.String(120), nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    total_compra = db.Column(db.Float, nullable=False)
    
    def __init__(self, id_producto, proveedor, producto, precio_unitario, cantidad, fecha=None, total_compra=0, ) -> None:
        self.id_producto = id_producto
        self.proveedor = proveedor
        self.producto = producto
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.fecha = fecha
        self.total_compra = total_compra
        
        
    def __repr__(self):
        return f"User({self.id}, '{self.id_producto}', '{self.proveedor}', '{self.producto}', '{self.precio_unitario}', '{self.cantidad}', '{self.fecha}', '{self.total_compra}')" 