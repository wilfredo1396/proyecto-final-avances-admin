from utils.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    unitcostpurchase = db.Column(db.Integer, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    unitcostsale = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    
    def __init__(self, provider, description, unitcostpurchase, Quantity, unitcostsale, date=None) -> None:
        self.provider= provider
        self.description = description
        self.unitcostpurchase = unitcostpurchase
        self.Quantity = Quantity
        self.unitcostsale = unitcostsale
        self.date = date
    

    def __repr__(self) -> str:
        return f"Compras({self.id}, '{self.provider}', '{self.description}', '{self.unitcostpurchase}', '{self.Quantity}', '{self.unitcostsale}', '{self.date}')"