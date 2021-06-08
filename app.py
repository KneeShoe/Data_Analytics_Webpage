from flask import Flask, render_template
from firebase import Firebase

config = {
  "apiKey": "AIzaSyAjzviH0PIn_p_Vn_4JOeosH87WXZ6h5Bk",
  "authDomain": "trial-e8fec.firebaseapp.com",
  "projectId": "trial-e8fec",
  "storageBucket": "trial-e8fec.appspot.com",
  "messagingSenderId": "358226149642",
  "databaseURL": "https://trial-e8fec-default-rtdb.firebaseio.com",
  "appId": "1:358226149642:web:debea6485c15ff449abaf3",
  "measurementId": "G-Z67W6VYVV1"
}

firebase = Firebase(config)
app = Flask(__name__)


@app.route('/')
def index():
    info = '["0","10000","5000","15000","10000","20000","15000","25000"]'
    info1 = '["50","30","15"]'
    return render_template("index.html", info=info, info1=info1)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/table')
def table():
    return render_template("table.html")


if __name__ == '__main__':
    app.run()
