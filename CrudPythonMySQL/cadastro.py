import mysql.connector
import pandas as pd

# Função para conectar ao banco de dados
def conectar_banco():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123", #Set your passwords
        database="Teste"
    )
    return conn

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Coletar dados do usuário
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    ano_nascimento = int(input("Digite o ano de nascimento do cliente: "))
    sexo = input("Digite o sexo do cliente (M/F): ").upper()

    # Executar o INSERT
    query = "INSERT INTO clientes (nome, email, ano_nascimento, sexo) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, ano_nascimento, sexo)
    cursor.execute(query, valores)

    # Salvar as mudanças
    conn.commit()
    print("Cliente cadastrado com sucesso!")

    # Fechar a conexão
    cursor.close()
    conn.close()

# Função para atualizar um cliente existente
def atualizar_cliente():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Coletar o ID do cliente a ser atualizado
    id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))

    # Verificar se o cliente existe
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        print(f"Cliente encontrado: {cliente}")
        # Coletar novos dados
        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
        novo_email = input("Digite o novo email (ou pressione Enter para manter o atual): ")
        novo_ano_nascimento = input("Digite o novo ano de nascimento (ou pressione Enter para manter o atual): ")
        novo_sexo = input("Digite o novo sexo (M/F) (ou pressione Enter para manter o atual): ").upper()

        # Manter os valores atuais se o usuário não digitar nada
        if not novo_nome:
            novo_nome = cliente[1]  # Nome atual
        if not novo_email:
            novo_email = cliente[2]  # Email atual
        if not novo_ano_nascimento:
            novo_ano_nascimento = cliente[3]  # Ano de nascimento atual
        else:
            novo_ano_nascimento = int(novo_ano_nascimento)  # Converter para inteiro
        if not novo_sexo:
            novo_sexo = cliente[4]  # Sexo atual

        # Executa o UPDATE
        query = "UPDATE clientes SET nome = %s, email = %s, ano_nascimento = %s, sexo = %s WHERE id = %s"
        valores = (novo_nome, novo_email, novo_ano_nascimento, novo_sexo, id_cliente)
        cursor.execute(query, valores)

        # Salva as mudanças
        conn.commit()
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")

    # Fechar a conexão
    cursor.close()
    conn.close()

# Função para mostrar os dados dos clientes
def mostrar_dados():
    conn = conectar_banco()
    query = "SELECT * FROM clientes"
    df = pd.read_sql(query, conn)
    print(df)
    conn.close()

# Função para excluir os dados dos clientes
def excluir_cliente():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Coleta o ID do cliente a ser atualizado
    id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))

    # Verificar se o cliente existe
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        print(f"Cliente encontrado: {cliente}")
        query = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(query, (id_cliente,))
        conn.commit()
        print("Cliente excluído com sucesso!")
    else:
        print("Cliente não encontrado.")

    # Fechar a conexão
    cursor.close()
    conn.close()

# Menu principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar novo cliente")
        print("2. Atualizar cliente existente")
        print("3. Mostrar dados dos clientes")
        print("4. Excluir dados dos clientes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            atualizar_cliente()
        elif opcao == "3":
            mostrar_dados()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
