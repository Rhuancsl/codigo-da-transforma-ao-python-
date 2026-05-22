from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conectar ao banco
def conectar():
    conn = sqlite3.connect("usuarios.db")
    conn.row_factory = sqlite3.Row
    return conn

# Criar tabela
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

criar_tabela()

# Cadastrar usuário
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, email)
        VALUES (?, ?)
    """, (nome, email))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Usuário salvo no banco!"
    })

# Listar usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    lista = []

    for usuario in usuarios:
        lista.append({
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"]
        })

    conn.close()

    return jsonify(lista)

if __name__ == "__main__":
    app.run(debug=True)