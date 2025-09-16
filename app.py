from flask import Flask, render_template, redirect, request
import pymysql

app = Flask(__name__)

def connection():
    return pymysql.connect(
        host="localhost", user="root", password="", database="library"
    )

@app.route("/")
def home():
    return render_template("add_book.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    conn = connection()
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    year = request.form["year"]
    with conn.cursor() as cur:
        sql = "INSERT INTO books (title, author, genre, year) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (title, author, genre, year))
        conn.commit()
    return redirect("/book_list")

@app.route("/book_list")
def book_list():
    conn = connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM books")
        data = cur.fetchall()
    return render_template("book_list.html", data=data)

@app.route("/delete_book/<int:id>")
def delete_book(id):
    conn = connection()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM books WHERE id=%s", (id,))
        conn.commit()
    return redirect("/book_list")

@app.route("/update_book/<int:id>")
def update_book(id):
    conn = connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM books WHERE id=%s", (id,))
        data = cur.fetchone()
    return render_template("update_book.html", data=data)

@app.route("/update_data", methods=["POST"])
def update_data():
    conn = connection()
    id = request.form["id"]
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    year = request.form["year"]
    with conn.cursor() as cur:
        sql = "UPDATE books SET title=%s, author=%s, genre=%s, year=%s WHERE id=%s"
        cur.execute(sql, (title, author, genre, year, id))
        conn.commit()
    return redirect("/book_list")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
