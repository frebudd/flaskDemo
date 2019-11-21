from flask import Flask ,render_template, request,flash,redirect,url_for,session,g,current_app,make_response
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired
from  wtforms import StringField,PasswordField,SubmitField,TextAreaField,RadioField,FileField
from wtforms.validators import DataRequired,EqualTo,Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import dataBase
from werkzeug.datastructures import CombinedMultiDict
import os
import json
import article_spider
import zhihuPic
import verify_code
from io import BytesIO
import hashlib
import frebudd_form




app = Flask(__name__)
bootstrap=Bootstrap(app)
app.secret_key="frebudd"


# 登录 首页
@app.route('/',methods=['GET','POST'])
def index():

    formLogin=frebudd_form.LoginForm()
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if session['image'].lower() != formLogin.code.data:
            flash("验证码错误")
            return redirect(url_for('index'))
        try:
            result = dataBase.selectUser(username, password)
            print(result)
            if result:
                if result[5]:
                    userPic = result[5].replace('/static/','')
                    session['userPic'] = userPic
                name= result[2]
                if result[6]:
                    introduction=result[6]
                    session['introduction'] = introduction
                session['name']=name
                session['username'] = username
                return redirect(url_for('index'))
            else:
                flash("账号或密码错误")
        except Exception as e:
            print(e)
            flash("服务器繁忙")
        return redirect(url_for('index'))
    return render_template('user.html',name=session.get('username'),form=formLogin)

# 用户注册
@app.route('/register',methods=['GET','POST'])
def register():
    form_reg = frebudd_form.LoginForm()
    if request.method=='POST':
        try:
            if form_reg.validate_on_submit():
                name = form_reg.name.data
                username = form_reg.username.data
                password = form_reg.password.data
                print(username, password)
                # 将用户添加入数据库
                result = dataBase.addUser(username, name, password)
                flash(result)
            else:
                flash("参数有误")
        except Exception as e:
            flash("注册失败")
            print(e)
        return redirect(url_for('register'))
    return render_template('register.html', form=form_reg)

# 用户注销
@app.route('/logout',methods=['GET','POST'])
def logout():
    if session.get('username'):
        session.clear()
    return redirect(url_for('index'))

# 管理员界面
@app.route("/admin",methods=["GET","POST"])
def admin():
    form = frebudd_form.admin_form()
    return render_template("admin.html",form=form)

# 修改用户信息
@app.route('/updateInfo',methods=['GET','POST'])
def updateInfo():
    form=frebudd_form.user_update_info(CombinedMultiDict((request.files, request.form)))
    if request.method=="POST":
        sex=request.form['sex']
        print(sex)
        headurl = form.headurl.data
        print(headurl)
        filename = headurl.filename
        print(filename)
        if form.validate_on_submit():
            name = form.name.data
            password = form.password.data
            sex = request.form['sex']
            headurl = form.headurl.data
            introduction = form.introduction.data
            filename = headurl.filename
            headurl.save(os.path.join('./static/userhead', filename))
            headurl = '/static/userhead/' + filename
            username = session['username']
            print(name,password,sex,headurl,introduction,username)
            dataBase.UpdateUser(name, password, sex, headurl, introduction, username)
            session.clear()
            flash("账号修改成功！请重新登录！")
            redirect(url_for("updateInfo"))
        else:
            flash("账号修改失败！")
            redirect(url_for("updateInfo"))

    return render_template('updateInfo.html',form=form)

# 用户发布信息
@app.route('/publish',methods=['GET','POST'])
def publish():
    form=frebudd_form.publish_form(CombinedMultiDict((request.files, request.form)))
    # 发布信息
    username = session['username']
    if request.method=='POST':
       if form.validate_on_submit():
           # 用户添加图片
           file = form.file.data
           print(file)
           try:
               # 用户添加图片
               file = form.file.data
               print(file)
               if file:
                   filename = file.filename
                   file.save(os.path.join('./static/photo-zhihu/', filename))
                   fileurl = '/static/photo-zhihu/' + filename
                   result = dataBase.userAddPic(filename, fileurl, username)
                   flash(result)
                   return redirect(url_for('publish'))

               # 用户添加文章
               file_article = form.file_article.data
               print(file_article)
               if file_article:
                   filename = file_article.filename
                   file_article.save(os.path.join('./static/article/', filename))
                   file_url = 'static/article/' + filename
                   result = dataBase.user_add_article(filename, file_url, username)
                   print(result)
                   flash(result)
                   return redirect(url_for('publish'))

               # 用户添加音乐
               file_music = form.file_music.data
               print(file_music)
               if file_music:
                   filename = file_music.filename
                   file_music.save(os.path.join('./static/music/', filename))
                   file_url = '/static/music/' + filename
                   result = dataBase.user_add_music(filename, file_url, username)
                   print(result)
                   flash(result)
                   return redirect(url_for('publish'))
           except Exception as e:
               print(e)
               flash("添加失败")
       else:
           flash("添加文件格式不正确")
       return redirect(url_for('publish'))

    # 展示发布信息
    pho_addr=dataBase.selectUserPic(username)
    # if pho_addr:
        # print(pho_addr)
    music_addr=dataBase.select_user_music(username)
    # if music_addr:
    #     print(music_addr[0])
    article_info=dataBase.select_user_article(username)
    # if article_info:
        # print(article_info)
    if article_info:
        for num in range(0, len(article_info)):
            with open(article_info[num]['art_addr'], 'r',encoding='utf-8')as f:
                content = f.read()
                article_info[num]['art_addr'] = content
                article_info[num]['art_cont'] = article_info[num]['art_cont'].replace(".txt", '')
    return render_template('publish.html',form=form,phoAddrs=pho_addr,music_addr=music_addr,article=article_info)

# ajax请求图片
@app.route('/photo/<page>',methods=['GET','POST'])
def photo(page):
    result=''
    try:
        result=dataBase.selectPic(page)
        print(result)
    except Exception as e:
        print(e)
    print(result)
    return result

# ajax请求音乐
@app.route('/music/<page>',methods=['GET','POST'])
def music(page):
    try:
        result=dataBase.selectMusic(page)
        print(result)
    except Exception as e:
        print(e)

    return result

# ajax请求文章
@app.route('/article/<page>',methods=['GET','POST'])
def article(page):
    result='1'
    mark=''
    print(page,type(page))
    data=request.get_data('data')
    print(data)
    if data:
        data = json.loads(data)
        mark = data["mark"]
        print(111)
    try:
        result=dataBase.select_article(page)
        print(result)
        if not mark:
            for num in range(0, len(result)):
                with open(result[num]['art_addr'], 'r', encoding='utf-8')as f:
                    content = f.read()
                    result[num]['art_addr'] = content
                    result[num]['art_cont'] = result[num]['art_cont'].replace(".txt", '')
        result = json.dumps(result)
    except Exception as e:
        print(e)
        result = '1'
    # print(result)
    return result


# 用户图片评论
@app.route('/comment_pic/<picId>',methods=['GET','POST'])
def comment_pic(picId):
    pic = dataBase.cmtPic(picId)
    print(pic)
    form = frebudd_form.LoginForm(CombinedMultiDict((request.files, request.form)))
    if request.method=='POST':
        comment = form.textarea.data
        try:
            dataBase.userCmt(picId, comment, session['username'])
            flash("success")
            return redirect(url_for('comment_pic',picId=picId))
        except Exception as e:
            flash("error")
    return render_template('comment.html',pic=pic,form=form,picId=picId)

# 获得用户的图片评论
@app.route('/get_cmt/<picId>',methods=['GET','POST'])
def get_cmt(picId):
    data =request.get_data('data')
    print(data,type(data))
    data = json.loads(data)
    page=data['page']
    cmt = dataBase.selectPicCmt(picId,page)
    print(cmt)
    return cmt

# 用户文章评论
@app.route('/comment_article/<articleId>',methods=['GET','POST'])
def comment_article(articleId):
    content=''
    article_addr = dataBase.cmt_article(articleId)
    article_name=article_addr.replace('static/article/','').replace('.txt','')
    print(article_addr)
    with open(article_addr, 'r', encoding='utf-8')as f:
        content = f.read()
    form = frebudd_form.LoginForm(CombinedMultiDict((request.files, request.form)))
    if request.method=='POST':
        comment = form.textarea.data
        try:
            dataBase.userCmt_article(articleId,comment,session['username'])
            flash("success")
            return redirect(url_for('comment_article',articleId=articleId))
        except Exception as e:
            flash("error")
    return render_template('comment.html',cont=content,article_name=article_name,form=form,articleId=articleId)

# 获得用户的文章评论
@app.route('/get_cmt_article/<articleId>',methods=['GET','POST'])
def get_cmt_article(articleId):
    data =request.get_data('data')
    print(data,type(data))
    data = json.loads(data)
    page=data['page']
    cmt = dataBase.selectArticleCmt(articleId,page)
    print(cmt)
    return cmt

# 用户音乐评论
@app.route('/comment_music/<musicId>',methods=['GET','POST'])
def comment_music(musicId):
    cmt_music = dataBase.cmt_music(musicId)
    cmt_music_name=cmt_music.replace('/static/music/','')
    print(cmt_music,type(cmt_music))
    form = frebudd_form.LoginForm(CombinedMultiDict((request.files, request.form)))
    if request.method=='POST':
        comment = form.textarea.data
        try:
            dataBase.userCmt_music(musicId, comment, session['username'])
            flash("success")
            return redirect(url_for('comment_music',musicId=musicId))
        except Exception as e:
            flash("error")
    return render_template('comment.html',cmt_music=cmt_music,cmt_music_name=cmt_music_name,form=form,musicId=musicId)

# 获得用户的音乐评论
@app.route('/get_cmt_music/<musicId>',methods=['GET','POST'])
def get_cmt_music(musicId):
    data =request.get_data('data')
    print(data)
    data = json.loads(data)
    page=data['page']
    cmt = dataBase.select_music_cmt(musicId,page)
    print(cmt)
    return cmt

# 用户点赞
@app.route('/praise',methods=['GET','POST'])
def dianzan():
    praise=''
    data =request.get_data('data')
    # print(data,type(data))
    data = json.loads(data)
    objId = data['objId']
    obj_type=data['obj_type']
    print(objId)
    praise=dataBase.pic_praise(objId,obj_type,session['username'])
    print(praise)
    return praise

# 管理员删除内容
@app.route('/delete/<type>',methods=['GET','POST'])
def delete(type):
    print(type)
    obj_id=request.get_data('data')
    print(obj_id)
    obj_id=json.loads(obj_id)
    obj_id=obj_id['obj_id']
    print(obj_id)
    result = dataBase.admin_delete(obj_id,type)
    return type

# 管理员使用爬虫添加信息
@app.route('/add_obj',methods=['GET','POST'])
def add_obj():
    data_obj=request.get_data('data') #获取ajax传来的数据
    print(data_obj)
    data_obj=json.loads(data_obj) #json解码ajax传来的数据
    data_value=data_obj['obj_data'] #获取爬虫网站地址
    data_type=data_obj['obj_type'] #获取爬取的类型
    print(data_value,data_type)
    try:
        if data_type == "article" and session['admin']:
            flash("请稍等")
            result = article_spider.get_book(data_value)  # 运行文章爬虫
            if result:
                result = dataBase.add_article(session['admin'])  # 将爬取到文件的信息写入数据库
                flash(result)
                return result
        if data_type == "photo" and session['admin']:
            flash("请稍等")
            result = zhihuPic.get_photo(data_value)
            if result:
                result = dataBase.addPic(session['admin'])
                flash(result)
                return result
    except Exception as e:
        print(e)
    flash("操作失败")
    return "hello"

# 用户删除自己发布的内容
@app.route('/user_delete_obj/<obj>/<id>',methods=['POST','GET'])
def user_delete_obj(obj,id):
    print(obj)
    print(id)
    result="what"
    if obj=='article':
        result=dataBase.user_delete(id,'article_info')
    elif obj =='photo':
        result=dataBase.user_delete(id,'photo')
    else:
        result=dataBase.user_delete(id,'music')
    return result

# 管理员查询用户图片评论
@app.route('/admin_pic_cmt/<page>',methods=['POST','GET'])
def admin_pic_cmt(page):
    result=''
    cmt_type=json.loads(request.get_data('data'))['cmt_type']
    print(cmt_type)
    result = dataBase.admin_cmt(page, cmt_type)
    return result

# 管理员删除用户评论
@app.route('/delete_cmt/',methods=['POST','GET'])
def delete_cmt():
    result=''
    data=request.get_data('data')
    data=json.loads(data)
    obj_type=data['obj_type']
    obj_id=data['obj_id']
    print(obj_type,obj_id)
    result=dataBase.admin_delete_cmt(obj_id,obj_type)
    print(result)
    return result

# 验证码
@app.route('/code',methods=['POST','GET'])
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

# 管理员登录界面
@app.route('/admin_login',methods=['POST','GET'])
def admin_login():
    form = frebudd_form.admin_login_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_name = form.user_name.data
            pass_word = form.pass_word.data
            code = form.verify_code.data
            print(user_name,pass_word,code)
            if session['image'].lower() != code.lower():
                flash('验证码错误')
                return redirect(url_for('admin_login'))
            result = dataBase.admin_login(user_name,pass_word)
            print(result)
            if result == '登录成功':
                session['admin']=user_name
                print(session['admin'])
                return render_template('admin.html')
            else:
                flash(result)
    return render_template('admin_login.html',form=form)

# 管理员查询管理用户
@app.route('/user_info/<page>',methods=['POST','GET'])
def user_info(page):
    result=''
    result =dataBase.user_info(page)
    print(result)
    return result

# 管理员删除用户
@app.route('/user_delete',methods=['POST','GET'])
def user_delete():
    result = ''
    data = request.get_data('data')
    data = json.loads(data)
    user_id = data['user_id']
    result = dataBase.admin_delete_user(user_id)
    return  result

#公告栏管理
@app.route('/carousel',methods=['POST','GET'])
def carousel():
    items={}
    items={'item_one':'one'}
    items={'item_two':'two'}
    items={'item_three':'three'}
    items=json.dumps(items)
    return items

if __name__ == '__main__':
    app.run(debug=True)

