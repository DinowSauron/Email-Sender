from app import app
from flask import render_template
from app.models.forms import LoginForm
from app.controllers import sendemail
from flask import request

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
    


@app.route("/sendForm", methods=["POST"])
def send_form():
    form = request.form
    # lembre-se de validar os campos! pode utilizar o flask wtf
    if sendemail.Send(form):
        return render_template("finish.html")
    else:
        return render_template("error.html")

"""
@app.route("/test", defaults={"name": None})
@app.route("/test/<str:name>", method=["GET"])
def test(name):
    if name:
        return f"Olá, {name}!"
    else:
        return "Olá Usuário!"
"""
