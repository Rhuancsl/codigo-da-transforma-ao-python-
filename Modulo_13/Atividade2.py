'from flask import Flask, request, jsonify'

app = 'Flask'(__name__)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    'dados = request.get_json()'

    'nome = dados.get("nome")'
    'email = dados.get("email")'

    return 'jsonify'({
        "mensagem": "Usuário cadastrado com sucesso",
        "usuario": {
            "nome": nome,
            "email": email,
        }
    })

if __name__ == "__main__":
    app.run(debug=True)