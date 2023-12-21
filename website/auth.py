from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("hello")
def home():
    return "<h1>Home Auth</h1>"

@auth.route("login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def signup():
    return "<p>sign-up</p>"