from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import User


class OrderCreateForm(FlaskForm):

    provider = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "provider"},
    )


    description = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "description"},
    )
    unitcostpurchase = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "unit cost purchase"},
    )
    
    Quantity = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Quantity"},
    )
    
    unitcostsale = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "unit cost sale"},
    )
    submit = SubmitField("create")

