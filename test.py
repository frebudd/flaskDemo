import pymysql


# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql= "select * from %s "
# cursor.execute(" select * from photo")
# db.commit()
# result = cursor.fetchall()
# print(result,type(result))
# # print(1)
#
# db.rollback()
# db.close()
# print(result[1],type(result[1]))
# result=str(result)
# print(result,type(result))
# result=result.replace("(","[").replace(")","]")
# print(result,type(result))
# print(list(result),type(result))

# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
# cursor = db.cursor()
# # print(headurl, username)
# headurl='/static/userhead/网页4第1张.jpg'
# username='test001'
# sql = "update user set headurl=%s where username=%s"
# try:
#     cursor.execute(sql, (headurl, username))
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()

# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
# cursor = db.cursor()
# sql= "select * from user where username=%s and password=%s"
# try:
#     cursor.execute(sql,('test001','123456'))
#     db.commit()
#     result=cursor.fetchone()
#     print(result)
#     # print(result[5],type(result[5]))
#     # print(result[5].replace('/static',''))
#     print(result[6])
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()

# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
# cursor = db.cursor()



# import os
#
# files = os.listdir('static/photo-zhihu')
# for file in files:
#     print(file)

# -*- coding: utf-8 -*-

# import os
#
# for root, dirs, files in os.walk('static/photo-zhihu'):
#     print(root)  # 当前目录路径
#     print(dirs)  # 当前路径下所有子目录
#     print(files)  # 当前路径下所有非目录子文件
import os

# files = os.listdir('static/photo-zhihu')
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
# cursor = db.cursor()
# sql="insert into photo(title,phoAddr) values (%s,%s)"
# try:
#     for file in files:
#         # print(file)
#         cursor.execute(sql,(file,'static/photo-zhihu/'+file))
#         db.commit()
# except:
#     db.rollback()
# db.close()
# time='0'
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select phoAddr from photo limit %s,5"
# try:
#     cursor.execute(sql, int(time))
#     db.commit()
#     result = cursor.fetchall()
#     print(result)
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()


# files = os.listdir('static/photo-zhihu')
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
# cursor = db.cursor()
# sql = "insert into photo(title,phoAddr) values (%s,%s)"
# try:
#     for file in files:
#         cursor.execute(sql, (file, 'static/photo-zhihu/' + file))
#         db.commit()
# except:
#     db.rollback()
# db.close()


# result = ''
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from photo where username=%s"
# try:
#     cursor.execute(sql, 'test001')
#     db.commit()
#     result = cursor.fetchall()
#     print(result)
#     print(type(result))
#     print(result[1]['phoAddr'])
# except Exception as e:
#     db.rollback()
# db.close()
# result = None
# files = os.listdir('static/music')
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
#                      cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "insert into music(title,musAddr) values (%s,%s)"
# try:
#     for file in files:
#         cursor.execute(sql, (file, 'static/music/' + file))
#         db.commit()
# except Exception as e:
#     db.rollback()
# db.close()
import json

# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
#                      cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from music limit %s,5"
# try:
#     cursor.execute(sql, int(0))
#     db.commit()
#     result = cursor.fetchall()
#     print(result)
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()
#
# json =json.dumps(result)
# print(json)

# result=None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
#                          cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from photo limit %s,5"
# try:
#     cursor.execute(sql, int(0))
#     db.commit()
#     result = cursor.fetchall()
#     result = json.dumps(result)
#         # print(result)
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()
# print(result)

# result = ''
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from photo where username=%s"
# try:
#     cursor.execute(sql, 'test001')
#     db.commit()
#     result = cursor.fetchall()
#     print(result)
#     result = json.dumps(result)
# except Exception as e:
#     db.rollback()
# db.close()
# print(result)


# user  add comment
# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
#                      cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "insert into cmt_pic(content,cmt_name,cmt_head) values (%s,%s,%s)"
# try:
#     cursor.execute(sql,('hello this comment','testone','itismyhead'))
#     db.commit()
# except Exception as e:
#     print(e)
# db.close()

# user select comment
# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from cmt_pic where pic_id=%s"
# try:
#     cursor.execute(sql, int(0))
#     db.commit()
#     result = cursor.fetchall()
#     result = json.dumps(result)
# except Exception as e:
#     print(e)
# db.close()
# print(result)

# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from photo where id=%s"
# try:
#     cursor.execute(sql, int(1748))
#     db.commit()
#     result = cursor.fetchall()
#     print(result,type(result))
#     result = json.dumps(result)
#     print(result,type(result))
# except Exception as e:
#     db.rollback()
# db.close()

# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from cmt_pic where pic_id=%s"
# try:
#     cursor.execute(sql, int(0))
#     db.commit()
#     result = cursor.fetchall()
#     result = json.dumps(result)
# except Exception as e:
#     print(e)
# db.close()
# print(result,type(result))

# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd', cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select * from cmt_pic where pic_id=%s limit %s,5"
# sql_count = "SELECT COUNT(*) FROM cmt_pic WHERE pic_id=%s"
# try:
#     cursor.execute(sql_count, int(1782))
#     db.commit()
#     count = cursor.fetchall()
#     if count[0]['COUNT(*)'] > 5:
#         cursor.execute(sql, (int(1782),0))
#         db.commit()
#         result = cursor.fetchall()
#         result = json.dumps(result)
# except Exception as e:
#     print(e)
# db.close()
# print(result)

# 先搜索是否存在，在判断是否添加
# result = None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
#                      cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql_add = "insert into praise_pic(pic_id,praise,user_id) values (%s,%s,%s)"
# select_praise = "select * from praise_pic where pic_id=%s and user_id=%s"
# sql_update = "update praise_pic set praise=%s"
# sql_count = "select count(*) from praise_pic where pic_id=%s and user_id=%s and praise=1"
# try:
#     cursor.execute(select_praise,('123','test1'))
#     db.commit()
#     result=cursor.fetchall()
#     if result:
#         print(result[0]['praise'])
#         if result[0]['praise']==1:
#             cursor.execute(sql_update,(int(0)))
#             db.commit()
#         elif result[0]['praise']==0:
#             cursor.execute(sql_update,(int(1)))
#             db.commit()
#     else:
#         cursor.execute(sql_add, ('123', '1', 'test1'))
#         db.commit()
#     cursor.execute(sql_count,('123','test1'))
#     db.commit()
#     result=cursor.fetchall()
#     print(result,type(result))
#     result=json.dumps(result)
#     print(result,type(result))
#
#
# except Exception as e:
#     print(e)
# db.close()
# result=None
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd',
#                          cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select *,(select count(*) ct from praise_pic where pic_id=photo.id and praise=1) as c from photo limit %s,5"
# try:
#     cursor.execute(sql, (int(1)))
#     db.commit()
#     result = cursor.fetchall()
#     print(result[0])
#     # result = json.dumps(result)
#     # print(result)
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()
# 获取当前时间
# import time
# get_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# print(get_time)

# import dataBase
# dataBase.addPic()

import dataBase
# dataBase.add_article()

# result= dataBase.select_article(2)
# print(len(result))
# for num in range(0,len(result)):
#     with open(result[num]['art_addr'],'r',encoding='utf-8')as f:
#         content=f.read()
#         result[num]['art_addr']=content


# print(result[1]['art_addr'],type(result[1]))
# with open(result[1]['art_addr'],'r',encoding='utf-8')as f:
#     content=f.read()
#     result[1]['art_addr']=content
#     print(result[1]['art_addr'])
#     print(content)

# result = dataBase.select_article(2)
# print(result)
# for num in range(0, len(result)):
#     with open(result[num]['art_addr'], 'r', encoding='utf-8')as f:
#         content = f.read()
#         result[num]['art_addr'] = content
#
# print(result)

# content=''
# article_addr = dataBase.cmt_article(141)
# print(article_addr)
# with open(article_addr, 'r', encoding='utf-8')as f:
#     content = f.read()
# print(content)

# result = ''
# db = pymysql.connect(host='localhost',user='root',password='',db='frebudd',cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = "select *,(select `name` from `user` where username=cmt_article.cmt_user) as com_name,(select headurl from `user` where username=cmt_article.cmt_user)as com_icon from cmt_article where article_id=%s limit %s,5"
# sql_count="SELECT COUNT(*) FROM cmt_article WHERE article_id=%s"
# try:
#     # cursor.execute(sql_count,int(10))
#     # db.commit()
#     # count=cursor.fetchall()
#     # if count[0]['COUNT(*)']>int(0):
#     #     cursor.execute(sql, (int(10),int(0)))
#     #     db.commit()
#     #     result = cursor.fetchall()
#     #     result = json.dumps(result)
#     cursor.execute(sql,(int(10),int(0)))
#     db.commit()
#     result = cursor.fetchall()
#     result = json.dumps(result)
# except Exception as e:
#     print(e)
# db.close()
# print(result)

# import time
#
# get_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
# print(get_time,type(get_time))
# print(time.time())
# files = os.listdir('static/article')
# db = pymysql.connect(host='localhost', user='root', password='', db='frebudd')
# cursor = db.cursor()
# sql = "insert into article_info(art_cont,art_addr,createDate,user_name) values (%s,%s,%s,%s)"
# sql_select = "SELECT * FROM article_info where art_cont=%s"
# try:
#     for file in files:
#         cursor.execute(sql_select,(file))
#         db.commit()
#         select_result=cursor.fetchall()
#         if not select_result:
#             cursor.execute(sql, (file, 'static/article/' + file, get_time, 'admin001'))
#             db.commit()
# except:
#     db.rollback()
# db.close()

# import hashlib
#
# data=b'asdasd'
# temp = hashlib.md5(data)
# print(temp.hexdigest())

asd='dsadsadsa'
asd=asd.replace('a','b').strip()
print(asd)