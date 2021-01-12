from flask import Flask, request
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, flash, redirect
import requests

# URL value modified from text document and a video that shows the Support OrgID
url = 'https://tntsfeqzp4a.sandbox.verygoodproxy.com/post'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


app = Flask(__name__)
app.config.from_object(Config)

# Initialization of Flask dataform for the web-form
class DataForm(FlaskForm):
    CCNum = StringField('Credit Card Number', validators=[DataRequired()])
    Expire = StringField('Expiration Date (MM-YY)', validators=[DataRequired()])
    CVV = StringField('CVV Value', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Flask uses "routes" to determine on what page items are rendered.
# Wasn't entirely sure how to add an onclick event to this Flask form.
@app.route("/", methods=['Get', 'POST'])
def submit():
    form = DataForm()
    if form.validate_on_submit():
        flash('Data Submitted'.format(
            form.CCNum.data[-4]))

        payload = request.form()
        r = requests.post(url, data=payload, headers=headers)
        r.json()
        return redirect('/')
    return render_template('index.html', title='Please fill these fields out', form=form)


if __name__ == '__main__':
    app.run()
