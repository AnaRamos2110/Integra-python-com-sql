from flask import Flask, jsonify
from conexao import criar_conexao  # usa seu arquivo de conexão existente

app = Flask(__name__)

# Rota para exibir todos os clientes
@app.route("/forncedores", methods=["GET"])
def listar_forncedores():
    try:
        conn = criar_conexao()
        cursor = conn.cursor(dictionary=True)  # retorna resultados como dicionário
        cursor.execute("SELECT * FROM fornecedores")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)