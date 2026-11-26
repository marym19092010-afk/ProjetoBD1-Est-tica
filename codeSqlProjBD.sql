CREATE DATABASE clinica_db;

USE clinica_db;

CREATE TABLE agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    servico VARCHAR(100) NOT NULL
);