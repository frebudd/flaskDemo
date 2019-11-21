from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_sql_demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/frebudd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
#     __tablename__ = 'photo'


@app.route('/')
def index():
    return "hello flask"

if __name__ == "__main__":


    # # 删除表
    # db.drop_all()
    # # 创建表
    # db.create_all()
    #
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
    db.reflect()
    allTable=db.get_tables_for_bind()
    print(allTable)
    print(allTable[1])
    # all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    # print(all_table)
    # print(all_table['users'])
    # print(db.get_tables_for_bind())
    # print(type(db.get_tables_for_bind()))
    # print(db.get_tables_for_bind()['Table'])
    # a=db.session.query(all_table['role']).all()
    # role = SQLAlchemy.Table('admin',autoload=True)
    app.run(debug=True)