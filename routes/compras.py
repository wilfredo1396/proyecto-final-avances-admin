from flask import Blueprint, render_template
from models.compras import Compra
from forms.comprasForm import NuevaCompra
from flask_login import login_required, current_user

compras = Blueprint("compras", __name__, url_prefix="/buy")

@compras.route("/")
@login_required
def home():
    lista_compras = Compra.query.all()
    return render_template("compras/home.html", items=lista_compras, user=current_user)

@compras.route("/new_sale")
@login_required
def NuevaCompra():
    return "Página para agregra una nueva compra"

@compras.route("/update_sale")
@login_required
def UpdateCompra():
    return "Página para actualizar detalle de compra"
    
