from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista em memória para simulação
clientes = []

@app.route("/fornecedores", methods=["POST"])
def add_cliente():
    data = request.get_json()
    listar_fornecedores.append(data)
    return jsonify({"mensagem": "Fornecedor cadastrado com sucesso!"}), 201

@app.route("/fornecedores", methods=["GET"])
def listar_fornecedores():
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(debug=True)