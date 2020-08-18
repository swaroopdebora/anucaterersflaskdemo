import os
from datetime import datetime
from flask import Flask, json, redirect, render_template, request, session, url_for, flash, g
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:RootUser@myfirstcluster.zhfps.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html", page_title="Ananya Caterers")


def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})
    
    f = open("userchat.txt", "a")
    f.write('"timestamp": {}, "from": {}, "message": {} \n' .format(now, username, message))


@app.route("/", methods=["GET", "POST"])
def chat():
 
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))
    return render_template("index.html")

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple')) 
print(users)
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('taskmanage'))
  
        return redirect(url_for('taskmanage'))

    return render_template("login.html", page_title="Login to Ananya Caterers")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
    return render_template("chat.html", username=username, chat_messages=messages)


@app.route("/ourspecialities")
def ourspecialities():
    data = []
    with open("data/dishes.json","r") as json_data:
        data = json.load(json_data)
    return render_template("ourspecialities.html", page_title="Our Specialities", dishes =data)


@app.route("/taskmanage")
def taskmanage():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("taskmanage.html",task=mongo.db.task.find() ,page_title = "Task Manager")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method =="POST":
        flash("Thank you {}, we have recieved your message!".format(request.form["name"]))
    return render_template ("contact.html", page_title = "Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Come work with us")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            )

