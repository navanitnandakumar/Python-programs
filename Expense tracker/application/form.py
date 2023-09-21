from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, RadioField
from wtforms.validators import DataRequired

class userinput(FlaskForm):
    type = RadioField("Type", validators = [DataRequired()], choices=[('income', 'Income'), ('expense', 'Expense')])
    category = StringField("Category", validators = [DataRequired()])
    amount = FloatField("Amount", validators = [DataRequired()])
    submit = SubmitField("Add")