from flask import Flask
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)  # type:Flask
app.secret_key = "DragonFire"


@app.before_request
def is_login():
    if request.path == "/login":
        return None

    if not session.get("user"):
        return redirect("/login")


@app.route("/login")
def login():
    return "Login"


@app.route("/index")
def index():
    return "Index"


@app.route("/home")
def home():
    return "Login"


app.run("0.0.0.0", 5000)
