from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index2.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            tasks.append(user_input)
        return render_template("success.html")
    
    return render_template("add.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")


if __name__ == "__main__":
    app.run()
