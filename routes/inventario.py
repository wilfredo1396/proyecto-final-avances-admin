from flask import Blueprint, render_template, redirect, url_for
from models.inventario import Inventario    
from forms.inventarioForm import Nuevo_Producto
from flask_login import login_required, current_user
from utils.db import db

productos = Blueprint("productos", __name__, url_prefix="/products")

@productos.route("/")
@login_required
def home():
    lista_productos = Inventario.query.all()
    return render_template("inventario/home.html", items=lista_productos, user=current_user)