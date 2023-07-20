from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ApplePeanutPig"

@app.route("/")
def index():
    flash("what's your name?") 
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET" ])
def greet():
    request.form['name_input']
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")