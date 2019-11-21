import pymysql
import json
import time
import os
import hashlib
# 用户注册
def addUser(username,name,password):
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    password=hashlib.md5(password.encode())
    cursor = db.cursor()
    sql = 'insert into user(username,name,password)values (%s,%s,%s)'
    sql_select = 'select * from user where username=%s'
    try:
        cursor.execute(sql_select,(username))
        db.commit()
        result = cursor.fetchall()
        if  not result:
            cursor.execute(sql, (username, name, passowrd))
            db.commit()
        else:
            return "用户名已注册"
    except:
        db.rollback()

    db.close()
    return "注册成功"

# 用户登录
def selectUser(username,password):
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    password=hashlib.md5(password.encode()).hexdigest()
    sql= "select * from user where username=%s and password=%s and delete_state=1"
    try:
        cursor.execute(sql,(username,password))
        db.commit()
        result=cursor.fetchone()
    except:
        db.rollback()
    db.close()
    return result

# 修改用户
def UpdateUser(name,password,sex,headurl,introduction,username):
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    password = hashlib.md5(password.encode()).hexdigest()
    cursor = db.cursor()
    print(headurl,username)
    sql = "update user set `name`=%s, password=%s, sex=%s, headurl=%s, introduction=%s  where username=%s"
    try:
        cursor.execute(sql,(name,password,sex,headurl,introduction,username))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()

# ajax添加图片栏信息
def selectPic(page):
    result=None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select *,(select count(*) ct from praise_all where obj_id=photo.id and praise=1 and obj_type='pic') as ct," \
          "(select headurl from `user`where username=photo.user_name )as user_icon," \
          "(select `name` from `user` where username=photo.user_name)as com_name," \
          "(select com_name from admin_info where username=photo.user_name)as admin_com_name," \
          "(select admin_icon from admin_info where username=photo.user_name)as admin_icon" \
          " from photo where delete_state=1 ORDER BY id DESC limit %s,5"
    try:
        cursor.execute(sql, int(page))
        db.commit()
        result = cursor.fetchall()
        result = json.dumps(result)
        # print(result)
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# ajax添加文章栏信息
def select_article(page):
    result=None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "SELECT *,(SELECT com_name FROM admin_info WHERE username=article_info.user_name) AS com_name," \
          "(SELECT admin_icon FROM admin_info WHERE username=article_info.user_name) AS admin_icon," \
          "(select count(*) ct from praise_all where obj_id=article_info.id and praise=1 and obj_type='article') as ct," \
          " (select `name` from `user` where username=article_info.user_name)as user_com_name," \
          "(select headurl from `user` where username=article_info.user_name)as user_icon FROM article_info where delete_state=1 ORDER BY id DESC limit %s,3"
    try:
        cursor.execute(sql, int(page))
        db.commit()
        result = cursor.fetchall()
        # result = json.dumps(result)
        # print(result)
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# ajax添加音乐栏信息
def selectMusic(page):
    result = None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select *,(select count(*) ct from praise_all where obj_id=music.id and praise=1 and obj_type='music') as ct, " \
          "(select headurl from `user` where `username`=music.user_name)as user_icon," \
          "(select admin_icon from admin_info where username=music.user_name)as admin_icon ," \
          "(select `name` from `user` where `username`=music.user_name)as user_com_name ," \
          "(select com_name from admin_info where username=music.user_name)as admin_com_name " \
          "from music where delete_state=1 ORDER BY id DESC limit %s,5"
    try:
        cursor.execute(sql, int(page))
        db.commit()
        result = cursor.fetchall()
        result =json.dumps(result)
        # print(result)
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result


# 管理员登录
def admin_login(user_name,password):
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    sql = "select * from admin_info where username=%s and admin_pwd=%s"
    try:
        cursor.execute(sql,(user_name,password))
        db.commit()
        result = cursor.fetchall()
        if result:
            return '登录成功'
        else:
            return '登录失败'
    except Exception as e:
        print(e)
        db.rollback()
        return '服务器繁忙'

# 管理员添加图片信息到数据库
def addPic(admin):
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    files = os.listdir('static/photo-zhihu')
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    sql = "insert into photo(title,phoAddr,createDate,user_name,delete_state) values (%s,%s,%s,%s,1)"
    select_sql="select * from photo where title=%s" #判断数据库中是否已经存在
    try:
        for file in files:
            cursor.execute(select_sql,(file))
            db.commit()
            select_result = cursor.fetchall()
            if not select_result:
                cursor.execute(sql, (file, 'static/photo-zhihu/' + file, get_time,admin))
                db.commit()

    except Exception as e:
        print(e)
        db.rollback()
        return "添加图片到数据库失败"
    db.close()
    return "添加图片到数据库成功"

# 管理员添加音乐到数据库
def addMusic():
    result=None
    files = os.listdir('static/music')
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql= "insert into music(title,musAddr) values (%s,%s)"
    try:
        for file in files:
            cursor.execute(sql, (file, 'static/music/' + file))
            db.commit()
    except Exception as e:
        db.rollback()
    db.close()

# 管理员添加文章信息到数据库
def add_article(admin):
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    files = os.listdir('static/article')
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    sql = "insert into article_info(art_cont,art_addr,createDate,user_name,delete_state) values (%s,%s,%s,%s,1)"
    sql_select = "SELECT * FROM article_info where art_cont=%s"
    try:
        for file in files:
            cursor.execute(sql_select, (file))
            db.commit()
            select_result = cursor.fetchall()
            if not select_result:
                cursor.execute(sql, (file, 'static/article/' + file, get_time, admin))
                db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        return "添加文章到数据库失败"
    db.close()
    return "添加文章到数据库成功"


# 用户发布图片
def userAddPic(title,fileAddr,username):
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    sql = "insert into photo(title,phoAddr,createDate,user_name,delete_state) values (%s,%s,%s,%s,1)"
    sql_select = "SELECT * FROM photo where title=%s"
    try:
        cursor.execute(sql_select,(title))
        db.commit()
        result=cursor.fetchall()
        if not result:
            cursor.execute(sql, (title, fileAddr, get_time, username))
            db.commit()
        else:
            return "已存在"
    except:
        db.rollback()
    db.close()
    return "操作成功"

# 搜索用户发布的照片
def selectUserPic(username):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql="select * from photo where user_name=%s and delete_state=1"
    try:
        cursor.execute(sql,username)
        db.commit()
        result=cursor.fetchall()
        # result = json.dumps(result)
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# 搜索用户发布的文章
def select_user_article(user_name):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql="select * from article_info where user_name=%s and delete_state=1"
    try:
        cursor.execute(sql,user_name)
        db.commit()
        result=cursor.fetchall()
        # result = json.dumps(result)
    except Exception as e:
        db.rollback()
    db.close()
    return result


# 用户上传文章
def user_add_article(file,file_addr,user_name):
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    sql = "insert into article_info(art_cont,art_addr,createDate,user_name,delete_state) values (%s,%s,%s,%s,%s)"
    sql_select = "SELECT * FROM article_info where art_cont=%s"
    try:

        cursor.execute(sql_select, (file))
        db.commit()
        select_result = cursor.fetchall()
        if not select_result:
            cursor.execute(sql, (file,file_addr,get_time,user_name,1))
            db.commit()
        else:
            return "已存在"
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return "操作成功"

# 用户上传音乐
def user_add_music(file,file_addr,user_name):
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
    cursor = db.cursor()
    sql = "insert into music(music_title,musAddr,createDate,user_name,delete_state) values (%s,%s,%s,%s,%s)"
    sql_select = "SELECT * FROM music where music_title=%s and user_name=%s"
    try:
        cursor.execute(sql_select, (file,user_name))
        db.commit()
        select_result = cursor.fetchall()
        if not select_result:
            cursor.execute(sql, (file, file_addr,get_time, user_name,1))
            db.commit()
        else:
            return "已存在"
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return "操作成功"

# 搜索用户上传音乐
def select_user_music(user_name):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql="select * from music where user_name=%s and delete_state=1"
    try:
        cursor.execute(sql,user_name)
        db.commit()
        result=cursor.fetchall()
        # result = json.dumps(result)
    except Exception as e:
        db.rollback()
    db.close()
    return result

# 搜索用户图片评论
def selectPicCmt(picId,page):
    result = ''
    db = pymysql.connect(host='localhost',user='root',password='',db='frebudd',cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select *,(select `name` from `user` where username=cmt_pic.cmt_user) as com_name,(select headurl from `user` where username=cmt_pic.cmt_user)as com_icon from cmt_pic where pic_id=%s and delete_state=1 limit %s,5"
    sql_count="SELECT COUNT(*) FROM cmt_pic WHERE pic_id=%s "
    try:
        cursor.execute(sql_count,int(picId))
        db.commit()
        count=cursor.fetchall()
        if count[0]['COUNT(*)']>int(page):
            cursor.execute(sql, (int(picId),int(page)))
            db.commit()
            result = cursor.fetchall()
            result = json.dumps(result)
    except Exception as e:
        print(e)
    db.close()
    return result

# 用户发表图片评论
def userCmt(picId,cmt_cont,cmt_user):
    result = None
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "insert into cmt_pic(pic_id,cmt_cont,cmt_user,`date`,delete_state) values (%s,%s,%s,%s,1)"
    try:
        cursor.execute(sql,(picId,cmt_cont,cmt_user,get_time))
        db.commit()
    except Exception as e:
        print(e)
    db.close()

# 用户发表文章评论
def userCmt_article(articleId,cmt_cont,cmt_user):
    result = None
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "insert into cmt_article(article_id,cmt_cont,cmt_user,`date`,delete_state) values (%s,%s,%s,%s,1)"
    try:
        cursor.execute(sql,(articleId,cmt_cont,cmt_user,get_time))
        db.commit()
    except Exception as e:
        print(e)
    db.close()

# 用户发表音乐评论
def userCmt_music(music_id,cmt_cont,cmt_user):
    result = None
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "insert into cmt_music(music_id,cmt_cont,create_date,cmt_user,delete_state) values (%s,%s,%s,%s,1)"
    try:
        cursor.execute(sql,(music_id,cmt_cont,get_time,cmt_user))
        db.commit()
    except Exception as e:
        print(e)
    db.close()

# 搜索用户文章评论
def selectArticleCmt(articleId,page):
    result = ''
    db = pymysql.connect(host='localhost',user='root',password='',db='frebudd',cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select *,(select `name` from `user` where username=cmt_article.cmt_user) as com_name,(select headurl from `user` where username=cmt_article.cmt_user)as com_icon from cmt_article where article_id=%s and delete_state=1 limit %s,5"
    sql_count="SELECT COUNT(*) FROM cmt_article WHERE article_id=%s"
    try:
        cursor.execute(sql_count,int(articleId))
        db.commit()
        count=cursor.fetchall()
        if count[0]['COUNT(*)']>int(page):
            cursor.execute(sql, (int(articleId),int(page)))
            db.commit()
            result = cursor.fetchall()
            result = json.dumps(result)
    except Exception as e:
        print(e)
    db.close()
    return result

# 搜索用户音乐评论
def select_music_cmt(musicId,page):
    result = ''
    db = pymysql.connect(host='localhost',user='root',password='',db='frebudd',cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select *,(select `name` from `user` where username=cmt_music.cmt_user) as com_name,(select headurl from `user` where username=cmt_music.cmt_user)as com_icon from cmt_music where music_id=%s and delete_state=1 limit %s,5"
    sql_count="SELECT COUNT(*) FROM cmt_music WHERE music_id=%s"
    try:
        cursor.execute(sql_count,int(musicId))
        db.commit()
        count=cursor.fetchall()
        if count[0]['COUNT(*)']>int(page):
            cursor.execute(sql, (int(musicId),int(page)))
            db.commit()
            result = cursor.fetchall()
            result = json.dumps(result)
    except Exception as e:
        print(e)
    db.close()
    return result
# 展示用户发表评论的图片
def cmtPic(picId):
    result=None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql="select * from photo where id=%s"
    try:
        db.commit()
        cursor.execute(sql,picId)
        result=cursor.fetchall()
        # result = json.dumps(result)
        result=result[0]['phoAddr']
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# 展示用户发表评论的音乐
def cmt_music(music_id):
    result=None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql="select * from music where id=%s"
    try:
        db.commit()
        cursor.execute(sql,music_id)
        result=cursor.fetchall()
        # result = json.dumps(result)
        result=result[0]['musAddr']
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# 展示用户发表评论的文章
def cmt_article(articleId):
    result=None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql="select * from article_info where id=%s"
    try:
        db.commit()
        cursor.execute(sql, articleId)
        result = cursor.fetchall()
        # result = json.dumps(result)
        result = result[0]['art_addr']
    except Exception as e:
        db.rollback()
    db.close()
    return result

# 用户点赞信息
def pic_praise(objId,obj_type,userId):
    # 先搜索是否存在，在判断是否添加
    result = None
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql_add = "insert into praise_all(obj_id,praise,user_id,obj_type) values (%s,%s,%s,%s)"
    select_praise = "select * from praise_all where obj_id=%s and user_id=%s and obj_type=%s"
    sql_update = "update praise_all set praise=%s where obj_id=%s and user_id=%s and obj_type=%s"
    sql_count = "select count(*) ct from praise_all where obj_id=%s and  praise=1 and obj_type=%s"
    try:
        cursor.execute(select_praise, (objId, userId,obj_type))
        db.commit()
        result = cursor.fetchall()
        if result:
            if result[0]['praise'] == 1:
                cursor.execute(sql_update, (int(0),objId,userId,obj_type))
                db.commit()
            elif result[0]['praise'] == 0:
                cursor.execute(sql_update, (int(1),objId,userId,obj_type))
                db.commit()
        else:
            cursor.execute(sql_add, (objId, '1', userId,obj_type))
            db.commit()
        cursor.execute(sql_count, (objId, obj_type))
        db.commit()
        result = cursor.fetchall()
        result = json.dumps(result)
        print(result)
    except Exception as e:
        print(e)
    db.close()
    return result

# 管理员删除
def admin_delete(obj_id,obj_type):
    result = ''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor=db.cursor()
    sql="update " + obj_type+ " set delete_state=0 where id=%s"
    # sql_test="update article_info set delete_state=0 where id=1"
    print(sql,(obj_type,obj_id))
    try:
        cursor.execute(sql,(obj_id))
        # cursor.execute(sql_test)
        db.commit()
    except Exception as e:
        print(e)
        return e
    return result

# 用户删除自己发布的内容
def user_delete(obj_id,obj_type):
    result = ''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor=db.cursor()
    sql="update "+obj_type+" set delete_state=0 where id=%s "
    try:
        cursor.execute(sql,obj_id)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    return 'success'

# 管理员查询评论
def admin_cmt(page,cmt_type):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor=db.cursor()
    sql_pic="select * from cmt_pic where delete_state=1 limit %s,5"
    sql_article = "select * from cmt_article where delete_state=1 limit %s,5"
    sql_music = "select * from cmt_music where delete_state=1 limit %s,5"
    try:
        if cmt_type=='pic':
            cursor.execute(sql_pic,(int(page)))
        if cmt_type=='article':
            cursor.execute(sql_article,(int(page)))
        if cmt_type=='music':
            cursor.execute(sql_music,(int(page)))
        db.commit()
        result=cursor.fetchall()
        result=json.dumps(result)
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# 管理员删除用户评论
def admin_delete_cmt(obj_id,obj_type):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql_pic_delete="update cmt_pic set delete_state=0 where id=%s"
    sql_article_delete="update cmt_article set delete_state=0 where id=%s"
    sql_music_delete="update cmt_music set delete_state=0 where id=%s"
    try:
        if obj_type=='pic':
            cursor.execute(sql_pic_delete,obj_id)
        if obj_type=='article':
            cursor.execute(sql_article_delete,obj_id)
        if obj_type=='music':
            cursor.execute(sql_music_delete,obj_id)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return '操作成功'

# 管理员管理用户
def user_info(page):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select * from `user` where delete_state=1 limit %s,5"
    try:
        cursor.execute(sql,int(page))
        db.commit()
        result = cursor.fetchall()
        result = json.dumps(result)
        print(result)
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
    return result

# 管理员删除用户
def admin_delete_user(user_id):
    result=''
    db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "update user set delete_state=0 where id=%s"
    try:
        cursor.execute(sql,int(user_id))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        return 'false'
    db.close()
    return 'success'
