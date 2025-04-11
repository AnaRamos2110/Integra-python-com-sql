# Sistema de Cadastro de Clientes com Tkinter e SQLite

Este é um sistema simples de cadastro de clientes utilizando a biblioteca Tkinter para a criação de uma interface gráfica e SQLite para armazenar os dados em um banco de dados.

## Funcionalidades

- **Inserir Cliente**: Permite adicionar um cliente informando o ID, Nome e Email.
- **Exibir Clientes**: Exibe uma lista de todos os clientes cadastrados no banco de dados.
- **Interface Gráfica**: Desenvolvida com Tkinter, proporcionando uma interface amigável para o usuário interagir com o sistema.

## Tecnologias

- **Python 3.x**
- **Tkinter**: Biblioteca para criar interfaces gráficas.
- **SQLite**: Banco de dados utilizado para armazenar as informações dos clientes.

## Instalação

1. Clone este repositório para sua máquina local:


```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git 
   ```
   

2. Certifique-se de ter o Python 3.x instalado em seu computador.

3. Execute o script Python:

    `python nome-do-arquivo.py`

4. O sistema irá abrir uma janela onde você pode adicionar clientes e consultar os clientes cadastrados.

## Como Funciona
1. **Tela Inicial**: Ao iniciar o programa, você verá três campos de entrada:

- ID do Cliente

- Nome do Cliente

- Email do Cliente

2. **Adicionar Cliente** : Preencha os campos e clique em "Adicionar cliente". Isso irá inserir os dados no banco de dados SQLite.

3. **Mostrar Clientes**: Clique em "Mostrar clientes" para visualizar todos os clientes cadastrados no banco de dados.

4. **Sair**: Para fechar o programa, clique em "Sair".

## Como Funciona o Código

1. Tkinter: Usado para criar a interface gráfica.

2. SQLite: Usado para armazenar e recuperar dados do banco de dados.

3. Funções:

[submit()]: Insere os dados no banco de dados.

[query()]: Exibe todos os registros no banco de dados.

### Conexão com o Banco de Dados

O banco de dados SQLite é armazenado no seguinte caminho:

`C:/dados/clientes.db`

Se o banco de dados não existir, o SQLite criará automaticamente o arquivo ao primeiro uso.

### Código Explicado
1. Tkinter: Usado para criar a interface gráfica.

2. SQLite: Usado para armazenar e recuperar dados do banco de dados.

3. Funções:

    - [submit()]: Insere os dados no banco de dados.

    - [query()]: Exibe todos os registros no banco de dados.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para enviar um pull request.

