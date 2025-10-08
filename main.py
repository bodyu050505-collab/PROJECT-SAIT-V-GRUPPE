import sqlite3
from flask import Flask
from flask import render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secretkey'

tasks = []

# инициализация базы данных
def init_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Usertasks (
                id INTEGER PRIMARY KEY,
                tasktext TEXT,
                username TEXT NOT NULL
                )
                ''')
    connection.commit()
    connection.close() # обязательно закрываем

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Обработка регистрации                                                    ЭТО НЕЙРОСЕТЬ НЕ ВЕДИТЕСЬ
        username = request.form.get("username", "")
        if username:
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Usertasks (username) VALUES (?)', (username,))
            connection.commit()
            connection.close()
            # Здесь можно добавить логику сохранения пользователя в базу данных    ЭТО НЕЙРОСЕТЬ НЕ ВЕДИТЕСЬ
            # Пока просто устанавливаем флаг, что пользователь зарегистрирован     ЭТО НЕЙРОСЕТЬ НЕ ВЕДИТЕСЬ
            session['user_registered'] = True
        return redirect("/")
    
    if 'visited_page' in session:
        return render_template("index2.html", tasks=tasks)
    else:
        session['visited_page'] = True
        return render_template("register.html")
    
                                                                # Тут потом добавлю добавление задач в дб
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

@app.route("/deletesession")
def deleteses():
    session.pop('visited_page', None)
    return redirect("/")

if __name__ == "__main__":
    app.run()
