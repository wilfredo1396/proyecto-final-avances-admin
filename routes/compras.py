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



@compras.route("/new/<int:id_producto>", methods=['GET', 'POST'])
@login_required
def NuevaCompra(id_producto):
    nombre_producto = Inventario.query.get(id_producto)
    form = Nueva_Compra()
    if form.validate_on_submit():
        id_producto = id_producto
        proveedor = form.proveedor.data
        producto = nombre_producto.producto
        precio_unitario = form.precio_unitario.data
        cantidad = form.cantidad.data
        fecha = form.fecha.data
        total_compra = precio_unitario * cantidad

        nuevaCompra = Compra(id_producto, proveedor, producto, precio_unitario, cantidad, fecha, total_compra)
        db.session.add(nuevaCompra)
        db.session.commit()
        
        nombre_producto.existencia = nombre_producto.existencia + cantidad
        db.session.commit()
        return redirect(url_for("compras.home"))
    return render_template("compras/nueva.html", form=form, user=current_user, id_producto=id_producto)


@compras.route("/delete/<int:id>/<int:id_producto>")
@login_required
def EliminarCompra(id, id_producto):
    nombre_producto = Inventario.query.get(id_producto)
    delete_compra = Compra.query.get(id)
    nombre_producto.existencia = nombre_producto.existencia - delete_compra.cantidad
    db.session.delete(delete_compra)
    db.session.commit()
    db.session.commit()
    return redirect(url_for("compras.home"))


@compras.route("/update/<int:id>", methods=['GET', 'POST'])
@login_required
def ActualizarCompra(id):
    compra_actual = Compra.query.get(id)
    form = Nueva_Compra()
    if form.validate_on_submit():
        compra_actual.id_producto = compra_actual.id_producto
        compra_actual.proveedor = form.proveedor.data
        compra_actual.producto = compra_actual.producto
        compra_actual.precio_unitario = form.precio_unitario.data
        compra_actual.cantidad = form.cantidad.data
        compra_actual.fecha = form.fecha.data
        compra_actual.total_compra = compra_actual.precio_unitario * compra_actual.cantidad
        db.session.commit()
        return redirect(url_for("compras.home"))
    return render_template("compras/actualizar.html", form=form, item=compra_actual, user=current_user, id=id)