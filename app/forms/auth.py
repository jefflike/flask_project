'''
__title__ = 'auth.py'
__author__ = 'Jeffd'
__time__ = '4/8/18 3:40 PM'
'''
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    nickname = StringField('昵称', validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])

    def validate_email(self, field):
        '''
        查找同名email
        wtform传入的field，即客户端传过来的email参数
        :param field:
        :return:
        '''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经被注册')

class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])
