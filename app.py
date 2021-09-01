from logging import info
from flask import Flask,request,render_template
import pickle

app=Flask(__name__)

@app.route('/')
def get_user_login_details():
  return render_template("login.html")
database={'sai':'123','anderson':'456','samuel':'789'}   

@app.route('/form_login',methods=['POST','GET'])
def login():
    user_name=request.form['username']
    pswd=request.form['password']
    if user_name not in database:
        return render_template('login.html',info='Invalid user name')
    if database[user_name]==pswd:
        return render_template('home.html',name=user_name)
    else:
        return render_template('login.html',info='Invalid Password')

if __name__ == "__main__":
    app.run()
        