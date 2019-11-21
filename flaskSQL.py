from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_sql_demo'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/frebudd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Role(db.Model):

    __tablename__ ='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    def __repr__(self):
        return 'Role  %s %s'%(self.id, self.name)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return 'User  %s %s  %s  %s'%(self.id, self.name, self.email, self.password)

# class Photo(db.Model):
#     # __tablename__ = 'photo'
#     db.Table('photo',)


@app.route('/')
def index():

    db.reflect()
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    result=db.session.query(all_table["roles"]).filter_by(id=1).all()
    print(result)
    print(type(result))
    ret = [x._asdict() for x in result]
    print(ret)
    print(type(ret))
    return str(result)
    # return ret
    # return result
if __name__ == "__main__":
    # Admin = db.Table('admin', metadata, autoload=True, autoload_with=engine)
    # # 删除表
    # db.drop_all()
    # # 创建表
    # db.create_all()

    # ro1 = Role(name='admin')
    # db.session.add(ro1)
    # db.session.commit()
    #
    # ro2 = Role(name='user')
    # db.session.add(ro2)
    # db.session.commit()
    #
    # us1 = User(name='wz' ,email="1234@qq.com", password='123456', role_id=ro1.id)
    # us2 = User(name='xz', email="12334@qq.com", password='1231456', role_id=ro2.id)
    # us3 = User(name='az', email="12434@qq.com", password='1235456', role_id=ro2.id)
    #
    # db.session.add_all([us1,us2,us3])
    # db.session.commit()

    # print(Role.query.all())
    # print(type(Role))

    # db.get_tables_for_bind()

    # all_table["roles"]

    # print(all_table)
    # for tableObj in db.get_tables_for_bind():
    #     print(tableObj)
    #     print(type(tableObj))
        # print(tableObj.query.all())

    app.run(debug=True)