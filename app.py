from flask import Flask, render_template , request ,flash , redirect, url_for, session, logging
import configFileGenerator
from src import dataFetcher

app = Flask(__name__)
data_fetched = None

@app.route("/")
def home():
    return redirect("http://127.0.0.1:5000/login")


@app.route('/login' , methods= ['GET','POST'])
def login():

    CONFIG_FILE_GENERATOR = configFileGenerator.ConfigFileGenerator()

    if(request.method== 'POST'):
        userDetail = request.form
        userName = userDetail['username']
        userPassword = userDetail['password']
        global data_fetched 
        data_fetched = CONFIG_FILE_GENERATOR.name_and_pass(name= userName, password=userPassword)
        print(data_fetched)
        return redirect("http://127.0.0.1:5000/dashboard")
    else:
        return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    
    global data_fetched
    print(data_fetched)
    return render_template('dashboard.html',data_fetched = data_fetched)


if __name__ == "__main__":
    app.run(debug=True)