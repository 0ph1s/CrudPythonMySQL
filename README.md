# Sistema de Gerenciamento de Clientes em Python com MySQL

Este repositório contém um sistema básico de gerenciamento de clientes desenvolvido em Python, utilizando o MySQL como banco de dados. O sistema permite realizar operações CRUD (Create, Read, Update, Delete) em uma tabela de clientes, incluindo cadastro, atualização, visualização e exclusão de registros.

## ⚠ Aviso
Este código foi desenvolvido **apenas para fins de aprendizado básico**. Ele não inclui validação de entrada, tratamento adequado de erros ou medidas de segurança, como proteção contra SQL Injection. **Não é recomendado para uso em produção.**

## 📌 Recomendação
Para um projeto real, considere utilizar frameworks como **Django** ou **Flask** e implementar medidas de segurança adequadas, como:
- Validação de entradas.
- Proteção contra SQL Injection.
- Autenticação e autorização.
- Tratamento de erros robusto.

## Funcionalidades
O sistema oferece as seguintes funcionalidades:
1. **Cadastrar novo cliente:**
   - Insere um novo cliente no banco de dados com nome, email, ano de nascimento e sexo.
2. **Atualizar cliente existente:**
   - Permite atualizar os dados de um cliente existente com base no ID.
3. **Mostrar dados dos clientes:**
   - Exibe todos os clientes cadastrados em formato de tabela usando `pandas`.
4. **Excluir cliente:**
   - Remove um cliente do banco de dados com base no ID.

## Como Executar
1. **Pré-requisitos:**
   - Python 3.x instalado.
   - MySQL Server instalado e configurado.
   - Biblioteca `mysql-connector-python` e `pandas` instaladas.
     
     ```bash
     pip install mysql-connector-python pandas
     ```
2. **Configuração do Banco de Dados:**
   - Crie um banco de dados chamado `Teste` no MySQL.
   - Crie uma tabela `clientes` com a seguinte estrutura:
     
     ```sql
     CREATE TABLE clientes (
         id INT AUTO_INCREMENT PRIMARY KEY,
         nome VARCHAR(100) NOT NULL,
         email VARCHAR(100) NOT NULL,
         ano_nascimento INT,
         sexo CHAR(1)
     );
     ```
3. **Executar o código:**
   - Clone o repositório:
     
     ```bash
     git clone https://github.com/seu-usuario/nome-do-repositorio.git
     ```
   - Execute o script Python:
     
     ```bash
     python gerenciamento_clientes.py
     ```

## Estrutura do Código
- **Conexão com o Banco de Dados:**
  - A função `conectar_banco` estabelece a conexão com o MySQL.
- **Operações CRUD:**
  - `cadastrar_cliente`: Insere um novo cliente.
  - `atualizar_cliente`: Atualiza os dados de um cliente existente.
  - `mostrar_dados`: Exibe todos os clientes cadastrados.
  - `excluir_cliente`: Remove um cliente do banco de dados.
- **Menu Interativo:**
  - O menu principal permite ao usuário escolher entre as operações disponíveis.

## Exemplo de Uso
1. Cadastre um novo cliente:
   ```
   Digite o nome do cliente: João Silva
   Digite o email do cliente: joao.silva@example.com
   Digite o ano de nascimento do cliente: 1990
   Digite o sexo do cliente (M/F): M
   ```
2. Atualize um cliente existente:
   ```
   Digite o ID do cliente que deseja atualizar: 1
   Digite o novo nome (ou pressione Enter para manter o atual): João Oliveira
   ```
3. Visualize todos os clientes:
   ```
   ID  Nome           Email                   Ano_Nascimento  Sexo
   1   João Oliveira  joao.silva@example.com  1990            M
   ```
4. Exclua um cliente:
   ```
   Digite o ID do cliente que deseja excluir: 1
   ```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novas funcionalidades.
