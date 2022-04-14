from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length



class Nueva_Compra(FlaskForm):
    proveedor = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=80),
        ],
        render_kw={"placeholder": "Proveedor"},
    )
    
    descripcion = StringField(
        validators=[
            InputRequired(),
            Length(min=5, max=120),
        ],
        render_kw={"placeholder": "Descripcion"},
    )
        
    precio_unitario = FloatField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Precio unitario"},
    )
    
    cantidad = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Cantidad de artículos"},
    )
    
    fecha = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=50),
        ],
        render_kw={"placeholder": "fecha"},
    )
    

    submit = SubmitField("agregar")