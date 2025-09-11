from flask import Flask, render_template_string
from conexao import criar_conexao_fornecedor

app = Flask(__name__)

# Template HTML para exibir os clientes
TABELA_HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Fornecedores</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f5f5f5; }
        table { border-collapse: collapse; width: 80%; margin: auto; background-color: #fff; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: center; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        h1 { text-align: center; color: #333; }
    </style>
</head>
<body>
    <h1>Lista de Fornecedores</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Telefone</th>
        </tr>
        {% for fornecedor in fornecedores %}
        <tr>
            <td>{{ fornecedor['id'] }}</td>
            <td>{{ fornecedor['nome'] }}</td>
            <td>{{ fornecedor['email'] }}</td>
            <td>{{ fornecedor['telefone'] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Rota para exibir clientes em HTML
@app.route("/fornecedores")
def clientes_html():
    try:
        conn = criar_conexao_fornecedor()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM fornecedores")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template_string(TABELA_HTML, fornecedores=fornecedores)
    except Exception as e:
        return f"<h2>Erro ao buscar fornecedor: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)