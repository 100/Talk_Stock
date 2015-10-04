from flask_wtf import Form
from wtforms import TextField, validators

class NumberForm(Form):
    hashtag = TextField("hashtag", [validators.required()])
