from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    CCNum = StringField('Credit Card Number', validators=[DataRequired()])
    Expire = StringField('Expiration Date (MM-YY)', validators=[DataRequired()])
    CVV = StringField('CVV Value', validators=[DataRequired()])
    submit = SubmitField('Submit')
