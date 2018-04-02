from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class search_form(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30, message='长度不匹配')])
    page = IntegerField(validators=[DataRequired(), NumberRange(min=1, max=99, message='页码不匹配')], default=1)