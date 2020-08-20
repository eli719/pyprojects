from flask import Flask,render_template,request
import  datetime
app = Flask(__name__)


@app.route("/")
def hello():
    return "ni"


@app.route("/user/<name>")
def user(name):
    return "ni,%s"%name


@app.route("/user/<int:id>")
def users(id):
    return "ni,%d 的你"%id


@app.route("/index")
def index():
    time = datetime.date.today()
    a = [1, 2, 3]
    task = {'a':'asd', 'b':'qwe', 'c':'zxc'}
    return render_template("aaa.html", a = a,c=time,task=task)


@app.route("/test")
def register():
    return render_template("bbb.html")


@app.route("/result", methods=['post','get'])
def registers():
    result = request.form
    return render_template("ccc.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)