from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        print(user_input)
    return render_template("add.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")


if __name__ == "__main__":
    app.run()
