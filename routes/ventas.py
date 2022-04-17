from flask import Blueprint, render_template, redirect, url_for
from models.ventas import Venta
from models.inventario import Inventario
from forms.ventasForm import Nueva_Venta
from flask_login import login_required, current_user
from utils.db import db

ventas = Blueprint("ventas", __name__, url_prefix="/sales")

@ventas.route("/")
@login_required
def home():
    lista_ventas = Venta.query.all()
    return render_template("ventas/home.html", items=lista_ventas, user=current_user)



@ventas.route("/new_sale/<int:id_producto>", methods=['GET', 'POST'])
@login_required
def NuevaVenta(id_producto):
    nombre_producto = Inventario.query.get(id_producto)
    form = Nueva_Venta()
    if form.validate_on_submit():
        id_producto = id_producto
        cliente = form.cliente.data
        producto = nombre_producto.producto
        precio_unitario = form.precio_unitario.data
        cantidad = form.cantidad.data
        fecha = form.fecha.data
        total_venta = precio_unitario * cantidad

        nuevaVenta = Venta(id_producto, cliente, producto, precio_unitario, cantidad, fecha, total_venta)
        db.session.add(nuevaVenta)
        db.session.commit()
        
        nombre_producto.existencia = nombre_producto.existencia - cantidad
        db.session.commit()
        return redirect(url_for("ventas.home"))
    return render_template("ventas/nuevo.html", form=form, user=current_user, id_producto=id_producto)


@ventas.route("/delete_sale/<int:id>/<int:id_producto>")
@login_required
def EliminarVenta(id, id_producto):
    nombre_producto = Inventario.query.get(id_producto)
    delete_venta = Venta.query.get(id)
    nombre_producto.existencia = nombre_producto.existencia + delete_venta.cantidad
    db.session.delete(delete_venta)
    db.session.commit()
    db.session.commit()
    return redirect(url_for("ventas.home"))

@ventas.route("/update/<int:id>/<int:id_producto>", methods=['GET', 'POST'])
@login_required
def ActualizarVenta(id, id_producto):
    existencia_actual = Inventario.query.get(id_producto)
    venta_actual = Venta.query.get(id)
    form = Nueva_Venta()
    if form.validate_on_submit():
        venta_actual.id_producto = venta_actual.id_producto
        venta_actual.cliente = form.cliente.data
        venta_actual.producto = venta_actual.producto
        venta_actual.precio_unitario = form.precio_unitario.data
        venta_actual.cantidad = form.cantidad.data
        venta_actual.fecha = form.fecha.data
        venta_actual.total_venta = venta_actual.precio_unitario * venta_actual.cantidad
        existencia_actual.existencia = existencia_actual.existencia + venta_actual.cantidad
        db.session.commit()
        db.session.commit()
        return redirect(url_for("ventas.home"))
    return render_template("ventas/actualizar.html", form=form, item=venta_actual, user=current_user, id=id, id_producto=id_producto)