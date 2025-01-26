from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

# to config app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure cs50 to use sqlite database
db = SQL("sqlite:///quiz.db")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwagrs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwagrs)

    return decorated_function


def apology(message, code=400):

    def escape(s):
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=69, bottom=escape(message)), code


@app.after_request
def after_request(response):
    """make sure that the response is'nt cached """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# DONE
@app.route("/")
@login_required
def index():
    return render_template("index.html")


# DONE
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        passwd = request.form.get("password")

        # check username given
        if not name:
            return apology("provide username",400)

        # ceck password given
        if not passwd:
            return apology("provide password", 400)

        # to ensure password & username is valid
        row = db.execute("select * from users where username = ?", name)

        if len(row) != 1 or not check_password_hash(row[0]["hash"], passwd):
            return apology("invalid username or password0", 400)

        session["user_id"] = row[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


# DONE
@app.route("/logout")
def logout():
    # forgot user id
    session.clear()

    # return to the login form via homepage
    return redirect("/")


# DONE
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("provide username")

        if not password:
            return apology("provide password")

        if not confirmation:
            return apology("provide confirmation of password")

        if password != confirmation:
            return apology("password & comfirmation did't match")

        record = db.execute("select username from users where username = ?", username)
        if record:
            return apology("username already taken")

        passwd = generate_password_hash(password)
        db.execute("insert into users(username, hash) values(?, ?)", username, passwd)
        data = db.execute("select id from users where username = ?", username)

        if data:
            session["user_id"] = data[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


# DONE
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    user_id = session["user_id"]

    _ = db.execute("select username from users where id = ?", user_id)
    name = _[0]["username"]
    data = db.execute("select quiz, sum(attempt) as attempt from quizy where user_id = ? group by quiz", user_id)

    return render_template("dasnboard.html", name=name, data=data)


# DONE
@app.route("/quiz", methods=["GET","POST"])
def quiz():
    return render_template("quiz.html")


# DONE
@app.route("/solution", methods=["GET","POST"])
def solution():
    return render_template("solution.html")


# DONE
@app.route("/history", methods=["GET"])
def history():
   user_id = session["user_id"]
   data = db.execute("select * from quizy where user_id = ?", user_id)
   return render_template("history.html", data=data)


# DONE
@app.route("/python_quiz", methods=["GET","POST"])
def python_quiz():
    user_id = session["user_id"]
    if request.method == "POST":
        flash("You completed the Quiz")
        return redirect("/")

    db.execute("insert into quizy(user_id, quiz) values(?, ?)", user_id, 'python')
    return render_template("python_quiz.html")


@app.route("/c_quiz", methods=["GET","POST"])
def c_quiz():
    user_id = session["user_id"]
    if request.method == "POST":
        flash("You completed the Quiz")
        return redirect("/")

    db.execute("insert into quizy(user_id, quiz) values(?, ?)", user_id, 'C')
    return render_template("c_quiz.html")


@app.route("/sql_quiz", methods=["GET","POST"])
def sql_quiz():
    user_id = session["user_id"]
    if request.method == "POST":
        flash("You completed the Quiz")
        return redirect("/")

    db.execute("insert into quizy(user_id, quiz) values(?, ?)", user_id, 'SQL')
    return render_template("sql_quiz.html")

@app.route("/web_frontPack_quiz", methods=["GET","POST"])
def web_frontPack_quiz():
    user_id = session["user_id"]
    if request.method == "POST":
        flash("You completed the Quiz")
        return redirect("/")

    db.execute("insert into quizy(user_id, quiz) values(?, ?)", user_id, 'Web Front Pack')
    return render_template("web_frontPack_quiz.html")


@app.route("/trivia_quiz", methods=["GET","POST"])
def trivia_quiz():
    user_id = session["user_id"]
    if request.method == "POST":
        flash("You completed the Quiz")
        return redirect("/")

    db.execute("insert into quizy(user_id, quiz) values(?, ?)", user_id, 'Trivia')
    return render_template("trivia_quiz.html")


# ===============================================================================

# DONE
@app.route("/python_solution", methods=["GET","POST"])
def python_solution():
    if request.method == "POST":
        flash("Hope you understand the concept")
        return redirect("/")

    return render_template("python_solution.html")

# DONE
@app.route("/c_solution", methods=["GET","POST"])
def c_solution():
    if request.method == "POST":
        flash("Hope you understand the concept")
        return redirect("/")

    return render_template("c_solution.html")


# DONE
@app.route("/sql_solution", methods=["GET","POST"])
def sql_solution():
    if request.method == "POST":
        flash("Hope you understand the concept")
        return redirect("/")

    return render_template("sql_solution.html")


# DONE
@app.route("/wed_frontPack_solution", methods=["GET","POST"])
def wed_frontPack_solution():
    if request.method == "POST":
        flash("Hope you understand the concept")
        return redirect("/")

    return render_template("wed_frontPack_solution.html")
