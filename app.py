from flask import Flask, request, render_template, redirect
from src import dataFormatter

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
data_fetched = None


# This route redirect to login page
@app.route("/")
def home():
    return redirect("https://statsxnat.herokuapp.com/login")


# Login Route
@app.route('/login' , methods= ['GET','POST'])
def login():

    # If request is a POST method then use the information to fetch data from the XNAT instance
    # Update the global data_fetched list and redirect to the dashboard 
    # where the global data_fetched will be used

    if(request.method== 'POST'):

        userDetail = request.form
        userName = userDetail['username']
        userPassword = userDetail['password']
        global data_fetched 
        global dataFormatter
        data_formatter = dataFormatter.Formatter(userName, userPassword)
        data_fetched = data_formatter.stats()

        if(data_fetched != None): # If the credential are right then add userName
            data_fetched.append(userName)
            print(data_fetched)

        return redirect("https://statsxnat.herokuapp.com/dashboard")

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
    app.run(threaded=True, port=5000)