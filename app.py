from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "mango_is-sweet"
@app.route("/hello")

def index():
    flash("Quel est ton nom?")
    return render_template("index.html")
    
@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello " + str(request.form['name_input']) + ", heureux de te revoir")
    return render_template("index.html")
