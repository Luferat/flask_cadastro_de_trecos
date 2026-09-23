'''
app.py
Aplicativo principal
'''

from flask import Flask, abort, render_template, request
import sqlite3
import random

app = Flask(__name__)


@app.route("/")
def index():

    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        contents = conn.execute("""
            SELECT id, name, photo 
            FROM thing
                WHERE status = 'on'
                ORDER BY created_at DESC
        """).fetchall()

    total = len(contents)

    return render_template(
        'index.html',
        contents=contents,
        total=total
    )


@app.route('/view/<int:thing_id>')
def view(thing_id):

    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        content = conn.execute("""
            SELECT *
            FROM thing
                WHERE status = 'on'
                AND id = ?
                ORDER BY created_at
        """, (thing_id,)).fetchone()

    if content is None:
        abort(404)

    return render_template(
        "view.html",
        content=content
    )


@app.route("/new", methods=['GET', 'POST'])
def new_thing():

    sended = False
    photo_number = random.randint(10, 999)
    thing_name = str()

    if request.method == 'POST':
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        location = request.form['location'].strip()
        photo = request.form['photo'].strip()

        with sqlite3.connect('database.db') as conn:
            conn.execute("""
                INSERT INTO thing (
                    name, description, location, photo
                ) VALUES (?, ?, ?, ?)
            """, (name, description, location, photo,))

            sended = True
            thing_name = name

    return render_template(
        "new.html",
        photo_number=photo_number,
        thing_name=thing_name,
        sended=sended
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
