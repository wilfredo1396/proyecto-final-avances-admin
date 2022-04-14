from utils.db import db 

class Inventario(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(120), nullable=False)
    existencia = db.Column(db.Integer, nullable=False)
    gasto_compra = db.Column(db.Float, nullable=False)
    ingreso_venta = db.Column(db.Float, nullable=False)

    
    def __init__(self, producto, existencia, gasto_compra, ingreso_venta) -> None:
        self.producto = producto
        self.existencia = existencia
        self.gasto_compra = gasto_compra
        self.ingreso_venta = ingreso_venta
      
        
    def __repr__(self):
        return f"User({self.id_producto}, '{self.producto}', '{self.existencia}', '{self.gasto_compra}', '{self.ingreso_venta}')" 