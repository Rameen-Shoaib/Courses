from flask import Flask, redirect, render_template, request, session, flash
from flask_session import Session
from cs50 import SQL

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///inspire.db")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    if not session.get("name"):
        return redirect("/login")

    notes = db.execute("SELECT notes FROM note WHERE name = (?)", session.get("name"))
    return render_template("index.html", notes=notes)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")

        exist_email = db.execute("SELECT password FROM data WHERE email = (?)", email)
        exist_name = db.execute("SELECT name FROM data WHERE email = (?)", email)

        value = [password['password'] for password in exist_email]
        for i in value:
            exist_email = i

        value2 = [name['name'] for name in exist_name]
        for j in value2:
            exist_name = j

        if exist_email and exist_email == password and exist_name == name:
            session["name"] = request.form.get("name").capitalize()
            return redirect("/index")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/index")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("Name")
        email = request.form.get("EMail")
        password = request.form.get("Password")

        exist_email = db.execute("SELECT * FROM data WHERE email = (?)", email)

        if exist_email:
            return render_template("user_exist.html")
        else:
            db.execute("INSERT INTO data (name, email, password) VALUES(?, ?, ?)", name, email, password)
            return redirect("/")

    return render_template("register.html")


@app.route("/user_exist")
def user_exist():
    return render_template("user_exist.html")


@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        notes = request.form.get("text")

        if (notes):
            db.execute("INSERT INTO note (name, notes) VALUES(?, ?)", session.get("name"), notes)

        if len(notes) != 0:
            return redirect("/index")

    return render_template("post.html")


@app.route("/delete_note", methods=["POST"])
def delete_note():
    note = request.form.get("note")
    db.execute("DELETE FROM note WHERE notes = ?", note)
    return redirect("/index")


@app.route("/edit_note_page", methods=["POST"])
def edit_note_page():
    note = request.form.get("note")
    return render_template("edit_note.html", note=note)


@app.route("/edit_note", methods=["POST"])
def edit_note():
    edited_note = request.form.get("edited_note")
    old_note = request.form.get("note")
    db.execute("UPDATE note SET notes = ? WHERE notes = ?", edited_note, old_note)
    return redirect("/index")