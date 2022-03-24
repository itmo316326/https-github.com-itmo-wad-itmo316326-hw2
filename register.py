from flask import Flask,request,redirect,session,render_template
import pymongo

app = Flask(__name__)
@app.route("/registeruser",methods=['GET','POST'])
def register():
    user_is_online = session.get('username')
    if user_is_online:
        return redirect(" http://localhost:5000/profile")
    else:
        if request.method =='POST':
            username = request.form['username']
            password = request.form['password']

            client = pymongo.MongoClient(host='localhost', port=27017)
            db = client.mydb
            collection = db.user
            user_is_online = collection.insert_one({"username":username,"password":password})
            if user_is_online:
                session['username'] = username
                return redirect(" http://localhost:5000/profile")
            else:
                message = 'hash value is null'
                return render_template('register.html',message=message)

if __name__ == '__main__':
    app.run(debug=True)
