from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Somewhat deprecated by including this in app.py inline rather than through an extends or import
class LoginForm(FlaskForm):
    CCNum = StringField('Credit Card Number', validators=[DataRequired()])
    Expire = StringField('Expiration Date (MM-YY)', validators=[DataRequired()])
    CVV = StringField('CVV Value', validators=[DataRequired()])
    submit = SubmitField('Submit')
