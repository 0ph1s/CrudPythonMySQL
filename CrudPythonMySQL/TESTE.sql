create database teste;

use teste;

/*Criar Tabela*/

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    ano_nascimento INT,
    sexo CHAR(1) -- 'M' para Masculino, 'F' para Feminino
);

/*Inserir Dados*/

INSERT INTO clientes (nome, email, ano_nascimento, sexo) VALUES
('João Silva', 'joao.silva@email.com', 1990, 'M'),
('Maria Oliveira', 'maria.oliveira@email.com', 1985, 'F'),
('Pedro Souza', 'pedro.souza@email.com', 1992, 'M'),
('Ana Costa', 'ana.costa@email.com', 1988, 'F'),
('Carlos Santos', 'carlos.santos@email.com', 1979, 'M'),
('Juliana Pereira', 'juliana.pereira@email.com', 1995, 'F'),
('Fernando Almeida', 'fernando.almeida@email.com', 1983, 'M'),
('Patrícia Lima', 'patricia.lima@email.com', 1991, 'F'),
('Ricardo Rocha', 'ricardo.rocha@email.com', 1987, 'M'),
('Amanda Martins', 'amanda.martins@email.com', 1993, 'F'),
('Lucas Gonçalves', 'lucas.goncalves@email.com', 1989, 'M'),
('Camila Ferreira', 'camila.ferreira@email.com', 1994, 'F'),
('Bruno Carvalho', 'bruno.carvalho@email.com', 1980, 'M'),
('Isabela Ribeiro', 'isabela.ribeiro@email.com', 1996, 'F'),
('Marcos Pinto', 'marcos.pinto@email.com', 1986, 'M'),
('Larissa Dias', 'larissa.dias@email.com', 1997, 'F'),
('Gustavo Moreira', 'gustavo.moreira@email.com', 1984, 'M'),
('Tatiane Castro', 'tatiane.castro@email.com', 1998, 'F'),
('Rafael Mendes', 'rafael.mendes@email.com', 1982, 'M'),
('Vanessa Nunes', 'vanessa.nunes@email.com', 1999, 'F');

/* SELECT */

SELECT * FROM clientes;

