from utils.db import db 

class Inventario(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(120), nullable=False)
    existencia = db.Column(db.Integer, nullable=False)


    
    def __init__(self, producto, existencia) -> None:
        self.producto = producto
        self.existencia = existencia
      
        
    def __repr__(self):
        return f"User({self.id_producto}, '{self.producto}', '{self.existencia}')" 