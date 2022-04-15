from flask import Blueprint, render_template, redirect, url_for
from models.compras import Compra
from models.inventario import Inventario
from forms.comprasForm import Nueva_Compra
from flask_login import login_required, current_user
from utils.db import db

compras = Blueprint("compras", __name__, url_prefix="/purchase")

@compras.route("/")
@login_required
def home():
    lista_compras = Compra.query.all()
    return render_template("compras/home.html", items=lista_compras, user=current_user)



@compras.route("/new/<int:id_product>", methods=['GET', 'POST'])
@login_required
def NuevaCompra(id_product):
    nombre_producto = Inventario.query.get(id_product)
    form = Nueva_Compra()
    if form.validate_on_submit():
        id_producto = id_product
        proveedor = form.proveedor.data
        producto = nombre_producto.producto
        precio_unitario = form.precio_unitario.data
        cantidad = form.cantidad.data
        fecha = form.fecha.data
        total_compra = precio_unitario * cantidad

        nuevaCompra = Compra(id_producto, proveedor, producto, precio_unitario, cantidad, fecha, total_compra)
        db.session.add(nuevaCompra)
        db.session.commit()
        return redirect(url_for("compras.home"))
    return render_template("compras/nueva.html", form=form, user=current_user, id_product=id_producto)


@compras.route("/delete_sale/<int:id>")
@login_required
def EliminarCompra(id):
    delete_compra = Compra.query.get(id)
    db.session.delete(delete_compra)
    db.session.commit()
    return redirect(url_for("compras.home"))



@compras.route("/update_sale")
@login_required
def UpdateCompra():
    return "Página para actualizar detalle de compra"
    
