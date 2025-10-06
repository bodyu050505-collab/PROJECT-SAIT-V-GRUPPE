from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/add", methods=["POST"])
def add():
    return render_template("add.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")


if __name__ == "__main__":
    app.run()
