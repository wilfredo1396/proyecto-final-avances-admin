from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from routes.compras import compras
from routes.inventario import productos
from routes.ventas import ventas
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from utils.loginManagerService import login_manager
from utils.db import db


app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)
Migrate(app, db)

app.register_blueprint(auth)
app.register_blueprint(compras)
app.register_blueprint(productos)
app.register_blueprint(ventas)