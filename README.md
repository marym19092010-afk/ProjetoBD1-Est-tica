#  Sistema de Agendamento - Clínica de Estética 

Projeto desenvolvido para a disciplina de Banco de Dados 1 (BD1), consistindo em uma aplicação web completa para gerenciamento e agendamento de serviços estéticos, integrando front-end, back-end em Python e banco de dados relacional MySQL.


##  Funcionalidades

- **Página Inicial (`/`):** Apresentação da clínica e navegação principal.
- **Cadastro de Agendamentos (`/formulario`):** Formulário web para registrar novos clientes e serviços solicitados diretamente no banco de dados.
- **Listagem de Registros (`/listar`):** Consulta em tempo real de todos os agendamentos cadastrados na tabela `agendamentos`.


##  Tecnologias Utilizadas

- **Back-end:** Python 3 & Flask
- **Banco de Dados:** MySQL (`clinica_db`)
- **Conector DB:** PyMySQL
- **Front-end:** HTML5 / CSS3
- **Versionamento:** Git & GitHub

---

##  Estrutura do Banco de Dados

Para rodar o projeto localmente, crie o banco de dados `clinica_db` e a tabela `agendamentos` no seu MySQL utilizando o script SQL abaixo:

``` sql
CREATE DATABASE IF NOT EXISTS clinica_db;
USE clinica_db;

CREATE TABLE agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    servico VARCHAR(100) NOT NULL
);
