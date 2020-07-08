from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://localhost:5432/chess"
app.secret_key = "jgfhdje78f9e78r9r789edfjlhwrjllk"
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(
    db.String(10000),
    primary_key = True
    )

    password = db.Column(
    db.String(10000)
    )

@app.route("/live")
def live():
    return render_template("live.html")
@app.route("/home")
def home():
    username = session.get("username") or "Unknown"
    return render_template("home.html", username = username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username = username).first()
        success = False
        if user and user.password == password:
            success = True

        if success:
            session["username"] = username
            return redirect("/home")
            pass
        return render_template("login.html", success = success, username = username)
    else:
        return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        message = None
        if password != confirm_password:
            message = "Passwords do not match"
        else:
            user = User.query.filter_by(username = username).first()
            if user:
                message = "User already exists"
            else:
                user = User(username = username, password = password)
                db.session.add(user)
                db.session.commit()
                session["username"] = username
                return redirect("/home")
        return render_template("signup.html", message = message)
    else:
        return render_template("signup.html")
