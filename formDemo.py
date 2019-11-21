from flask import Flask ,render_template, request,flash,make_response,session,redirect,url_for
from flask_wtf import FlaskForm,RecaptchaField
from  wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo
import verify_code
from io import BytesIO
import hashlib

app = Flask(__name__)
app.secret_key="frebudd"
# 表单和flash消息闪回
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username,password,password2]):
            # return "信息不完整"
            flash(u"信息不完整")
        elif password2 !=password:
            flash(u"密码不一致")
            # return "密码不一致"

        else:
            flash(u"登录成功")
            # return "登录成功"


    return render_template('formDemo.html')


# wtf表单的显示
class LoginForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired()])
    password2 = PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password')])
    verify_code = StringField('验证码:',validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/register',methods=['GET','POST'])
def login():
    formLogin = LoginForm()
    username=''
    if request.method == 'POST':
        if formLogin.validate_on_submit():
            # username = request.form.get("username")
            # password = request.form.get("password")
            # password2 = request.form.get("password2")
            username =formLogin.username.data
            password = formLogin.password.data
            print(hashlib.md5(password.encode()).hexdigest())
            code = formLogin.verify_code.data.lower()
            if session['image'].lower() !=code:
                flash('验证码不正确')
                return redirect(url_for('login'))
            print(username,password)
            flash("登录成功")
        else:
            flash("参数有误")
    return render_template('formDemo.html',form=formLogin)


@app.route('/code')
def get_code():
    image, code = verify_code.get_verify_code()
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = code
    print(code)
    print(response)
    return response

if __name__ == '__main__':
    app.run(debug=True)