from flask import Flask,request,render_template,redirect, session
import pymongo

app = Flask(__name__)
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.mydb
        collection = db.user
        useronline = collection.find({"username":username,"password":password}).count()
        if useronline:
            session['username'] = username
            return redirect(" http://localhost:5000/profile")
        else:
            message = "Failed Login"
            return render_template('login.html',message=message)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
