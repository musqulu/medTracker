# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:43:36 2021

@author: flo17
"""

from flask import Flask, request, render_template
import pyrebase

config = {
    "apiKey": "AIzaSyB5K3RQhJX9057a-qXDCcTFT1tqKryn5ug",
    "authDomain": "neurosphere-webapp.firebaseapp.com",
    "databaseURL": "https://neurosphere-webapp.firebaseio.com",
    "projectId": "neurosphere-webapp",
    "storageBucket": "neurosphere-webapp.appspot.com",
    "messagingSenderId": "638567925423",
    "appId": "1:638567925423:web:2e98b0dbb9a02cbeb9f65a"
    }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

#email = input('Please enter your email\n')
#password = input('Please enter your password\n')

#user = auth.create_user_with_email_and_password(email, password)


#auth.get_account_info(user['idToken'])
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)

app = Flask(__name__, )#template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        print("login")
        email = request.form['mail']
        password = request.form['pass']
        auth.sign_in_with_email_and_password(email, password)
        #print('login successful')
        return 'Login successful'
    

    return render_template("login.html")




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        print("login")
        email = request.form['mail']
        password = request.form['pass']
        auth.create_user_with_email_and_password(email, password)
        #print('signup successful')
        return 'signup successful'
    
    return render_template("signup.html")


@app.route('/timer')
def timer():
    return render_template("timer.html")

"""
# # decorator to wrap the function
# @app.route('/')
# @app.route('/<user>')
# def index(user=None):
#     return render_template("user.html", user=user)



# @app.route('/meditation')
# def meditation():
#     return '<h2>Meditation does not require you to sit cross-legged.</h2>'

# @app.route('/profile/<name>')
# def profile(name):
#     #return '<h2>hey there {}</h2>'.format(name)
#     return render_template("profile.html", name = name)

# @app.route('/session/<int:user_id>')
# def session(user_id):
#     return '<h2>Session-ID: {}</h2>'.format(user_id)

# @app.route("/timer", methods=['GET', 'POST'])
# def timer():
#     if request.method == 'POST':
#         return "post yay"
#     else:
#         return "get"
"""


if __name__ == "__main__":
    app.run(debug = True)



