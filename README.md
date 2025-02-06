# Customer Management System in Python with MySQL  

This repository contains a basic customer management system developed in Python, using MySQL as the database. The system allows CRUD (Create, Read, Update, Delete) operations on a customer table, including registration, updating, viewing, and deleting records.  

## ⚠ Warning  
This code was developed **for basic learning purposes only**. It does not include input validation, proper error handling, or security measures such as SQL Injection protection. **It is not recommended for production use.**  

## 📌 Recommendation  
For a real project, consider using frameworks like **Django** or **Flask** and implementing proper security measures, such as:  
- Input validation.  
- SQL Injection protection.  
- Authentication and authorization.  
- Robust error handling.  

## Features  
The system offers the following features:  
1. **Register a new customer:**  
   - Inserts a new customer into the database with name, email, birth year, and gender.  
2. **Update an existing customer:**  
   - Allows updating a customer’s details based on their ID.  
3. **Display customer data:**  
   - Shows all registered customers in a table format using `pandas`.  
4. **Delete a customer:**  
   - Removes a customer from the database based on their ID.  

## How to Run  
1. **Prerequisites:**  
   - Python 3.x installed.  
   - MySQL Server installed and configured.  
   - `mysql-connector-python` and `pandas` libraries installed.  
     
     ```bash
     pip install mysql-connector-python pandas
     ```  
2. **Database Setup:**  
   - Create a database named `Teste` in MySQL.  
   - Create a `clientes` table with the following structure:  
     
     ```sql
     CREATE TABLE clientes (
         id INT AUTO_INCREMENT PRIMARY KEY,
         nome VARCHAR(100) NOT NULL,
         email VARCHAR(100) NOT NULL,
         ano_nascimento INT,
         sexo CHAR(1)
     );
     ```  
3. **Run the Code:**  
   - Clone the repository:  
     
     ```bash
     git clone https://github.com/your-username/repository-name.git
     ```  
   - Run the Python script:  
     
     ```bash
     python gerenciamento_clientes.py
     ```  

## Code Structure  
- **Database Connection:**  
  - The `conectar_banco` function establishes a connection with MySQL.  
    
- **CRUD Operations:**  
  - `cadastrar_cliente`: Inserts a new customer.  
  - `atualizar_cliente`: Updates an existing customer’s details.  
  - `mostrar_dados`: Displays all registered customers.  
  - `excluir_cliente`: Removes a customer from the database.  
    
- **Interactive Menu:**  
  - The main menu allows the user to choose between available operations.  

## Usage Example  
1. Register a new customer:  
   
   ```
   Enter the customer's name: João Silva
   Enter the customer's email: joao.silva@example.com
   Enter the customer's birth year: 1990
   Enter the customer's gender (M/F): M
   ```  
   
3. Update an existing customer:  
   
   ```
   Enter the ID of the customer you want to update: 1
   Enter the new name (or press Enter to keep the current one): João Oliveira
   ```  
   
5. View all customers:  
   
   ```
   ID  Name           Email                   Birth_Year  Gender
   1   João Oliveira  joao.silva@example.com  1990        M
   ```  
   
7. Delete a customer:  
   
   ```
   Enter the ID of the customer you want to delete: 1
   ```  

## Contributions  
Contributions are welcome! Feel free to open issues or submit pull requests with improvements, fixes, or new features.  
