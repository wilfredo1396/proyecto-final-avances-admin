from utils.db import db 

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proveedor = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(120), nullable=False)
    precio_unitario = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    total_compra = db.Column(db.Integer, nullable=False)
    
    def __init__(self, proveedor, descripcion, precio_unitario, cantidad, fecha=None, total_compra=0, ) -> None:
        self.proveedor = proveedor
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.fecha = fecha
        self.total_compra = total_compra
        
        
    def __repr__(self):
        return f"User({self.id}, '{self.proveedor}', '{self.descripcion}', '{self.precio_unitario}', '{self.cantidad}', '{self.fecha}', '{self.total_compra}')" 