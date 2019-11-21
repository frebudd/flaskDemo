from flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Length


# wtf表单
class LoginForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired(), Length(6, 12, message=u'账号长度在6到12位')])
    password = PasswordField('密码：',validators=[DataRequired(), Length(6, 12, message=u'密码长度在6到12位')])
    password2 = PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password'),Length(6, 12, message=u'密码长度在6到12位')])
    submitL = SubmitField('登录')
    submitR = SubmitField('注册')