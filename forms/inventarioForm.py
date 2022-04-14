from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length



class Nuevo_Producto(FlaskForm):
    producto = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=120),
        ],
        render_kw={"placeholder": "Producto"},
    )
    
    existencia = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Cantidad en existencia"},
    )


    submit = SubmitField("agregar")