from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# =========================
# BANCO
# =========================

def conectar():
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # Usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
    """)

    # Posts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            conteudo TEXT,
            usuario_id INTEGER
        )
    """)

    # Comentários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT,
            post_id INTEGER,
            usuario_id INTEGER
        )
    """)

    conn.commit()
    conn.close()

criar_tabelas()

# =========================
# CADASTRAR USUÁRIO
# =========================

@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, email)
        VALUES (?, ?)
    """, (dados["nome"], dados["email"]))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Usuário criado!"
    })

# =========================
# LOGIN
# =========================

@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE email = ?
    """, (dados["email"],))

    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        return jsonify({
            "mensagem": "Login realizado!"
        })

    return jsonify({
        "erro": "Usuário não encontrado"
    }), 404

# =========================
# CRIAR POST
# =========================

@app.route("/posts", methods=["POST"])
def criar_post():
    dados = request.get_json()

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts (titulo, conteudo, usuario_id)
        VALUES (?, ?, ?)
    """, (
        dados["titulo"],
        dados["conteudo"],
        dados["usuario_id"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Post criado!"
    })

# =========================
# LISTAR POSTS
# =========================

@app.route("/posts", methods=["GET"])
def listar_posts():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")

    posts = cursor.fetchall()

    lista = []

    for post in posts:
        lista.append({
            "id": post["id"],
            "titulo": post["titulo"],
            "conteudo": post["conteudo"]
        })

    conn.close()

    return jsonify(lista)

# =========================
# CRIAR COMENTÁRIO
# =========================

@app.route("/comentarios", methods=["POST"])
def comentar():
    dados = request.get_json()

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO comentarios (texto, post_id, usuario_id)
        VALUES (?, ?, ?)
    """, (
        dados["texto"],
        dados["post_id"],
        dados["usuario_id"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Comentário criado!"
    })

# =========================
# LISTAR COMENTÁRIOS
# =========================

@app.route("/comentarios", methods=["GET"])
def listar_comentarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM comentarios")

    comentarios = cursor.fetchall()

    lista = []

    for comentario in comentarios:
        lista.append({
            "id": comentario["id"],
            "texto": comentario["texto"]
        })

    conn.close()

    return jsonify(lista)

# =========================
# EXECUTAR
# =========================

if __name__ == "__main__":
    app.run(debug=True)