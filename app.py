from flask import Flask, request, render_template, redirect
from statsXNAT import dataFormatter

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
user_name = ""
user_password = ""
instance_url = ""

# This route redirect to login page
@app.route("/")
def home():
    return redirect("https://statsXNAT.herokuapp.com/login")


# Login Route
@app.route('/login' , methods= ['GET','POST'])
def login():

    # If request is a POST method then use the information to fetch data from the XNAT instance
    # Update the global data_fetched list and redirect to the dashboard 
    # where the global data_fetched will be used

    if(request.method== 'POST'):

        user_detail = request.form
        global user_name
        global user_password
        global instance_url
        user_name = user_detail['username']
        user_password = user_detail['password']
        instance_url = user_detail['instance_url']

        return redirect("https://statsXNAT.herokuapp.com/dashboard")

    else:

        return render_template('login.html')


# Dashboard route
@app.route('/dashboard')
def dashboard():
    
    global user_password
    global user_password
    global instance_url

    data_formatter = dataFormatter.Formatter(user_name, user_password, instance_url)
    data_fetched = data_formatter.stats()

    if(data_fetched != None): 
        # If the credential are right then add userName and
        # send the data to html
        data_fetched.append(user_name)
        print(data_fetched)
        return render_template('dashboard.html', data_fetched = data_fetched)
    else:
        print("Exit")
        return render_template('error.html')



if __name__ == "__main__":
     app.run(debug = True, port=5000)