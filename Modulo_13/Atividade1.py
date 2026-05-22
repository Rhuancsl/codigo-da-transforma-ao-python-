'from flask import Flask, jsonify'

app = 'Flask'(__name__)

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return 'jsonify'({
        "mensagem": "Olá! Servidor Flask funcionando!"
    })

if __name__ == "__main__":
    app.run(debug=True)