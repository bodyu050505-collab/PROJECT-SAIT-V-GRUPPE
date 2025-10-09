import sqlite3
from flask import Flask
from flask import render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'your-permanent-secret-key-here-12345'

tasks = []
users = []

# инициализация базы данных
def init_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usertasks (
            id INTEGER PRIMARY KEY,
            tasktext TEXT NOT NULL,
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
            session['user_registered'] = True
            session['username'] = username
            users.append(username)
            print(users)
        return redirect("/")
    
    if 'visited_page' in session:
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        username = session.get('username')
        if username:
            cursor.execute('SELECT id, tasktext FROM Usertasks WHERE username = ?', (username,))
        tasks = cursor.fetchall()
        task_list = [{'id': task[0], 'text': task[1]} for task in tasks] # тут да нейросеть признаю слабость
        connection.close()
        return render_template("index2.html", tasks=task_list)
    else:
        session['visited_page'] = True
        return render_template("register.html")
    
                                                                # Тут потом добавлю добавление задач в дб
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")    
        if user_input:  # проверяем что есть пользователь
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            username = session.get('username')
            cursor.execute('INSERT INTO Usertasks (tasktext, username) VALUES (?, ?)', (user_input, username))
            connection.commit()
            connection.close()
        return render_template("success.html")
    
    return render_template("add.html", users=users)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        username = session.get('username')
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        task_id = request.form.get('task_id')
        cursor.execute("DELETE FROM Usertasks WHERE id = ? AND username = ?", (task_id, username))
        return redirect("/")
    return render_template("delete.html")

@app.route("/deletesession")
def deleteses():
    session.pop('visited_page', None)
    return redirect("/")

if __name__ == "__main__":
    app.run()
