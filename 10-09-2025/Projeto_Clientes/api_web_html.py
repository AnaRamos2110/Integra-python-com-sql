from flask import Flask, render_template_string
from conexao import criar_conexao

app = Flask(__name__)

# Template HTML para exibir os clientes
TABELA_HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Clientes</title>
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
    <h1>Lista de Clientes</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Telefone</th>
        </tr>
        {% for cliente in clientes %}
        <tr>
            <td>{{ cliente['id'] }}</td>
            <td>{{ cliente['nome'] }}</td>
            <td>{{ cliente['email'] }}</td>
            <td>{{ cliente['telefone'] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Rota para exibir clientes em HTML
@app.route("/clientes")
def clientes_html():
    try:
        conn = criar_conexao()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template_string(TABELA_HTML, clientes=clientes)
    except Exception as e:
        return f"<h2>Erro ao buscar clientes: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)