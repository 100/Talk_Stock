from flask_wtf import Form
from wtforms import TextField, validators

class NumberForm(Form):
    number = TextField("number", [validators.required()])
