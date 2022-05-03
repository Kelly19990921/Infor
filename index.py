import random
from aiohttp import request
from flask import Flask,request
from sqlalchemy import true

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<string:name>")
def hello(name):
    return f"<p style='text-align:center;margin-top:100px;'>早安，{name}您好！！</p>"

@app.route("/add/<string:x>/<string:y>")
def add(x, y):
    return f"<p style='text-align:center;margin-top:100px;'>{x} + {y} ={int(x)+int(y)}</p>"

@app.route("/add/<int:n>")
def sum(n):
    x=0
    s=""
    for i in range(1,n):
        x+=i
        s+=str(i)+"+"
    x+=n
    s+=str(n)+"="+str(x)
    return f"<p style='text-align:center;margin-top:100px;'>{s}</p>"

@app.route("/a")
def a():
    return "<p>阿巴</p>"

@app.route("/lucky")
def lucky():
    m=int(request.args.get('m'))
    d=int(request.args.get('d'))
    r='<img src="https://picsum.photos/200/300">'
    s=(m*2+d)%3
    if s == 0:
        return r+"<br>普通"
    elif s ==1:
        return r+"<br>吉"
    elif s==2:
        return r+"<br>大吉"

@app.route("/play")
def play():
    m=int(request.args.get('m'))
    d=random.randint(1,3)
    r='<img src="https://picsum.photos/200/300">'
    if m==1:
        r+="<br>玩家：剪刀"
        if d==1:
            r+="<br>電腦：剪刀<br>平手"
        elif d==2:
            r+="<br>電腦：石頭<br>電腦贏"
        elif d==3:
            r+="<br>電腦：布<br>玩家贏"
    elif m==2:
        r+="<br>玩家：石頭"
        if d==1:
            r+="<br>電腦：剪刀<br>玩家贏"
        elif d==2:
            r+="<br>電腦：石頭<br>平手"
        elif d==3:
            r+="<br>電腦：布<br>電腦贏"
    elif m==3:
        r+="<br>玩家：布"
        if d==1:
            r+="<br>電腦：剪刀<br>電腦贏"
        elif d==2:
            r+="<br>電腦：石頭<br>玩家贏"
        elif d==3:
            r+="<br>電腦：布<br>平手"
    return f"<p style='text-align:center;margin-top:100px;'>{r}</p>"

if __name__=='__main__':
    app.run(debug=True)