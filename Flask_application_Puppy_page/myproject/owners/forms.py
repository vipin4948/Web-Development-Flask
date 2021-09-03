# forms @ owners

from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    
    name = StringField("Name of owner : ")
    pup_id = IntegerField("Id of puppy: ")
    submit = SubmitField("ADD Owner")
