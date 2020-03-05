from flask import Flask, request, render_template, redirect
import configFileGenerator
from src import dataFetcher

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
data_fetched = None


# This route redirect to login page
@app.route("/")
def home():
    return redirect("http://127.0.0.1:5000/login")


# Login Route
@app.route('/login' , methods= ['GET','POST'])
def login():

    CONFIG_FILE_GENERATOR = configFileGenerator.ConfigFileGenerator()

    # If request is a POST method then use the information to fetch data from the XNAT instance
    # Update the global data_fetched list and redirect to the dashboard 
    # where the global data_fetched will be used

    if(request.method== 'POST'):
        userDetail = request.form
        userName = userDetail['username']
        userPassword = userDetail['password']
        global data_fetched 
        data_fetched = CONFIG_FILE_GENERATOR.name_and_pass(name= userName, password=userPassword)

        if(data_fetched != None): # If the credential are right then add userName
            data_fetched.append(userName)
            print(data_fetched)
        return redirect("http://127.0.0.1:5000/dashboard")
    else:
        return render_template('login.html')


# Dashboard route
@app.route('/dashboard')
def dashboard():
    
    global data_fetched

    # If the data_fetched is None result in error in login credentials

    if(data_fetched != None):
        print(data_fetched)
        return render_template('dashboard.html', data_fetched = data_fetched)
    else:
        return "Please login again with correct credentials no data found "



if __name__ == "__main__":
    app.run(debug=True)