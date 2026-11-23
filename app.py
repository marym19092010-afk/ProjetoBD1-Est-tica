import pymysql
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# Função para conectar ao seu banco de dados MySQL
def conectar_db():
  return pymysql.connect(
      host="localhost",
      user="root",
      password="",  # Substitua pela senha do seu MySQL
      port=3306,
      database="clinica_db",  # Nome do banco de dados
      cursorclass=pymysql.cursors.DictCursor,
  )


# Rota 1: Página Inicial (Home)
@app.route("/")
def index():
  return render_template("inedex.html")


# Rota 2: Formulário (Exibe o form e salva os dados no banco ao enviar)
@app.route("/formulario", methods=["GET", "POST"])
def formulario():
  if request.method == "POST":
    nome = request.form["nome"]
    email = request.form["e-mail"]  # Nome exato do input no seu HTML
    servico = request.form["servico"]

    conexao = conectar_db()
    with conexao.cursor() as cursor:
      sql = "INSERT INTO agendamentos (nome, email, servico) VALUES (%s, %s, %s)"
      cursor.execute(sql, (nome, email, servico))
      conexao.commit()
    conexao.close()

    return redirect(url_for("listar"))

  return render_template("foumulario BD1.html")


# Rota 3: Listar os dados cadastrados do banco
@app.route("/listar")
def listar():
  conexao = conectar_db()
  with conexao.cursor() as cursor:
    cursor.execute("SELECT * FROM agendamentos")
    dados = cursor.fetchall()
  conexao.close()

  return render_template("listar.html", agendamentos=dados)


if __name__ == "__main__":
  app.run(debug=True)
