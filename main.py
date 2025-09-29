from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")


if __name__ == "__main__":
    app.run()
