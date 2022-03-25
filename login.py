import secrets

from flask import Flask, request, render_template, redirect, session, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret

client = MongoClient('localhost', 27017)
db = client.wad


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pass_hash_code = generate_password_hash(password)
        is_user_online = db.users.find_one({"username": username, "password": pass_hash_code})
        if is_user_online:
            session['username'] = username
            return redirect(url_for("profile"))
        else:
            message = "Failed Login"
            return render_template('login.html', message=message)
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pass_hash_code = generate_password_hash(password)
        user_is_online = db.users.insert_many([{"username": username, "password": pass_hash_code} for _ in range(1)])
        if user_is_online:
            session['username'] = username
            return redirect(url_for("profile"))
        else:
            message = 'User not registered'
            return render_template('register.html', message=message)
    return render_template('register.html')


@app.route("/profile")
def profile():
    if session.get("username"):
        return render_template('profile.html')
    else:
        return render_template('login.html')


@app.route("/logout")
def log_out():
    session.clear()
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
