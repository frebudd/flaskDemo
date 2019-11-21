from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index1():
#     return '<h1>hello world</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello world %s</h1>' %name

@app.route('/')
def index():
    url_str="www.suprise.com"
    name = "Frebudd"
    mylist=[1,3,5,7]
    mydict={'name':"dave",'age':"22"}
    return render_template("demo.html",url_str=url_str, name=name, mylist=mylist, mydict=mydict)

@app.route('/photo/<page>',methods=['GET','POST'])
def photo(page):
    try:
        time2=0
        result=dataBase.selectPic(time2)
        print(result,type(result))
        result=str(result).replace("'",'"')
        # print(result)
    except Exception as e:
        pass
    return page
if __name__ == '__main__':
    app.run(debug=True)