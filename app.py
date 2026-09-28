'''
app.py
Aplicativo principal
'''

from flask import Flask, abort, flash, redirect, render_template, request, url_for
import sqlite3
import random

app = Flask(__name__)

app.secret_key = '_use_uma_secret_key_de_verdade_aqui_e_use_dotenv_em_deploy_'

sitename = "Cadastro de Trecos"


@app.errorhandler(404)
def not_found(error):

    if request.path.startswith("/api/"):
        return {
            "error": {
                "code": 404,
                "message": "Recurso não encontrado."
            }
        }, 404

    return render_template(
        "404.html",
        title=f'{sitename} - Página não encontrada',
    ), 404


@app.route("/api/things")
@app.route("/")
def index():

    page = request.args.get("p", 1, type=int)

    per_page = 18
    offset = (page - 1) * per_page

    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row

        contents = conn.execute("""
            SELECT id, name, photo
            FROM thing
            WHERE status = 'on'
            ORDER BY created_at DESC
            LIMIT ? OFFSET ?
        """, (per_page, offset)).fetchall()

        total = conn.execute("""
            SELECT COUNT(*)
            FROM thing
            WHERE status = 'on'
        """).fetchone()[0]

    pages = (total + per_page - 1) // per_page

    # Resposta para API, caso a rota seja chamada com /api/things
    if request.path.startswith("/api/"):
        return {
            "data": [dict(content) for content in contents],
            "pagination": {
                "total": total,
                "page": page,
                "per_page": per_page,
                "pages": pages
            }
        }

    # Resposta para a rota normal, caso seja chamada com /
    return render_template(
        'index.html',
        contents=contents,
        total=total,
        page=page,
        pages=pages,
        page_css='index.css',
        title=sitename
    )


@app.route("/api/things/<int:thing_id>")
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

    # Resposta para API, caso a rota seja chamada com /api/things
    if request.path.startswith("/api/"):
        return {
            "data": dict(content),
        }

    return render_template(
        "view.html",
        content=content,
        title=f'{sitename} - {content["name"]}'
    )


@app.route("/api/things", methods=["POST"])
@app.route("/new", methods=["GET", "POST"])
def new_thing():

    if request.method == "POST":

        # Dados
        if request.path.startswith("/api/"):
            data = request.get_json()
        else:
            data = request.form

        name = data["name"].strip()
        description = data["description"].strip()
        location = data["location"].strip()
        photo = data["photo"].strip()

        # INSERT
        with sqlite3.connect("database.db") as conn:
            cursor = conn.execute("""
                INSERT INTO thing (
                    name, description, location, photo
                ) VALUES (?, ?, ?, ?)
            """, (name, description, location, photo))

            thing_id = cursor.lastrowid

        # Response
        if request.path.startswith("/api/"):
            return {
                "id": thing_id,
                "name": name,
                "description": description,
                "location": location,
                "photo": photo
            }, 201

        flash("Registro cadastrado com sucesso!", "success")

        return redirect(
            url_for("view", thing_id=thing_id)
        )

    # GET
    photo_number = random.randint(10, 999)

    return render_template(
        "new.html",
        photo_number=photo_number,
        title=f'{sitename} - Novo registro'
    )


@app.route("/edit/<int:thing_id>", methods=["GET", "POST"])
@app.route("/api/things/<int:thing_id>", methods=["PUT"])
def edit(thing_id):

    # Busca o registro
    with sqlite3.connect("database.db") as conn:
        conn.row_factory = sqlite3.Row

        thing = conn.execute("""
            SELECT *
            FROM thing
            WHERE status = "on"
              AND id = ?
        """, (thing_id,)).fetchone()

    if thing is None:
        abort(404)

    # Atualização
    if request.method == "POST" or request.method == "PUT":

        # Dados
        if request.path.startswith("/api/"):
            data = request.get_json()
        else:
            data = request.form

        name = data["name"].strip()
        description = data["description"].strip()
        location = data["location"].strip()
        photo = data["photo"].strip()

        # UPDATE
        with sqlite3.connect("database.db") as conn:
            conn.execute("""
                UPDATE thing
                SET
                    name = ?,
                    description = ?,
                    location = ?,
                    photo = ?
                WHERE status = "on"
                  AND id = ?
            """, (name, description, location, photo, thing_id))

        # Response
        if request.path.startswith("/api/"):
            return {
                "id": thing_id,
                "name": name,
                "description": description,
                "location": location,
                "photo": photo
            }

        flash("Registro atualizado com sucesso!", "success")

        return redirect(
            url_for("view", thing_id=thing_id)
        )

    # GET → formulário HTML
    return render_template(
        "edit.html",
        content=thing,
        title=f'{sitename} - Editar registro'
    )


@app.route("/api/things/<int:thing_id>", methods=["DELETE"])
@app.route("/delete/<int:thing_id>", methods=["GET"])
def delete(thing_id):

    # Verifica se o registro existe
    with sqlite3.connect("database.db") as conn:
        conn.row_factory = sqlite3.Row

        thing = conn.execute("""
            SELECT id
            FROM thing
            WHERE status = "on"
              AND id = ?
        """, (thing_id,)).fetchone()

    if thing is None:
        abort(404)

    # Soft delete
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            UPDATE thing
            SET status = "del"
            WHERE status = "on"
              AND id = ?
        """, (thing_id,))

    # Response da API
    if request.path.startswith("/api/"):
        return {
            "id": thing_id,
            "status": "del"
        }

    # Response HTML
    flash("Registro apagado com sucesso!", "success")

    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title=f'{sitename} - Sobre...'
    )


if __name__ == "__main__":
    app.run(debug=True)
