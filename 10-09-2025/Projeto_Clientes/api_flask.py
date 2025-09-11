from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista em memória para simulação
clientes = []

@app.route("/clientes", methods=["POST"])
def add_cliente():
    data = request.get_json()
    clientes.append(data)
    return jsonify({"mensagem": "Cliente recebido com sucesso!"}), 201

@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(debug=True)