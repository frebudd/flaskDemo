from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired
from  wtforms import StringField,PasswordField,SubmitField,TextAreaField,RadioField,FileField
from wtforms.validators import DataRequired,EqualTo,Length

# 管理员登录表单
class admin_login_form(FlaskForm):
    user_name = StringField("管理员账号", validators=[DataRequired()])
    pass_word = PasswordField("管理员密码",validators=[DataRequired()])
    verify_code = StringField("验证码",validators=[DataRequired()])
    submit = SubmitField("登录")


class LoginForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired()])
    name = StringField('社区名称:',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired()])
    password2 = PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password')])
    submitR = SubmitField('注册')
    submitL = SubmitField('登录')
    submitU = SubmitField('确定修改')
    introduction = TextAreaField('个人简介:')
    headurl = FileField("上传头像",validators=[FileAllowed(['jpg','png','gif'])])
    textarea=TextAreaField()
    mysubmit=SubmitField('提交')
    code = StringField("验证码：",validators=[DataRequired()])

# 用户修改信息表单
class user_update_info(FlaskForm):
    name = StringField('社区名称:', validators=[DataRequired()])
    password = PasswordField('密码：', validators=[DataRequired()])
    password2 = PasswordField('确认密码：', validators=[DataRequired(), EqualTo('password')])
    introduction = TextAreaField('个人简介:',validators=[DataRequired()])
    headurl = FileField("上传头像", validators=[FileAllowed(['jpg', 'png', 'gif'])])
    submitU = SubmitField('确定修改')


# 用户发布信息表单
class publish_form(FlaskForm):
    file=FileField("上传图片",validators=[FileAllowed(['jpg','png','gif'])])
    file_article=FileField("上传文章",validators=[FileAllowed(['txt'])])
    file_music=FileField("上传音乐",validators=[FileAllowed(['mp3','m4a'])])

class admin_form(FlaskForm):
    text = StringField(validators=[DataRequired()])