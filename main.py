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

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        idx_str = request.form.get("idx")
        try:
            idx = int(idx_str)
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        except (TypeError, ValueError):
            pass
        return redirect("/")
    return render_template("delete.html")


if __name__ == "__main__":
    app.run()
