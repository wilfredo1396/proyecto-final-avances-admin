from utils.db import db 

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, nullable=False)
    cliente = db.Column(db.String(80), nullable=True)
    producto = db.Column(db.String(120), nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    total_venta = db.Column(db.Float, nullable=False)
    
    def __init__(self, id_producto, cliente, producto, precio_unitario, cantidad, fecha=None, total_venta=0, ) -> None:
        self.id_producto = id_producto
        self.cliente = cliente
        self.producto = producto
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.fecha = fecha
        self.total_venta = total_venta
        
        
    def __repr__(self):
        return f"User({self.id}, '{self.id_producto}', '{self.cliente}', '{self.producto}', '{self.precio_unitario}', '{self.cantidad}', '{self.fecha}', '{self.total_venta}')" 