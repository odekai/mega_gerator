from flask import Flask, render_template, request, redirect, url_for, session
from gerador_senha import gerar_senha
import json, os

app = Flask(__name__)
app.secret_key = 'segredo123'
usuarios_path = 'usuarios.json'
senhas_path = 'senhas.json'

def carregar_usuarios():
    if not os.path.exists(usuarios_path):
        return {}
    with open(usuarios_path, 'r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(usuarios_path, 'w') as f:
        json.dump(usuarios, f)

def carregar_senhas():
    if not os.path.exists(senhas_path):
        return {}
    with open(senhas_path, 'r') as f:
        return json.load(f)

def salvar_senhas(senhas):
    with open(senhas_path, 'w') as f:
        json.dump(senhas, f)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuarios = carregar_usuarios()
        user = request.form["usuario"]
        senha = request.form["senha"]
        if user in usuarios and usuarios[user] == senha:
            session["usuario"] = user
            return redirect(url_for("main"))
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos.")
    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        usuarios = carregar_usuarios()
        user = request.form["usuario"]
        senha = request.form["senha"]
        if user in usuarios:
            return render_template("cadastro.html", erro="Usuário já existe.")
        usuarios[user] = senha
        salvar_usuarios(usuarios)
        return redirect(url_for("login"))
    return render_template("cadastro.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    if "usuario" not in session:
        return redirect(url_for("login"))
    usuario = session["usuario"]
    senhas = carregar_senhas()
    user_senhas = senhas.get(usuario, [])
    if request.method == "POST":
        rede = request.form["rede"]
        senha_gerada = gerar_senha()
        user_senhas.append({"rede": rede, "senha": senha_gerada})
        senhas[usuario] = user_senhas
        salvar_senhas(senhas)
    return render_template("main.html", usuario=usuario, senhas=user_senhas)

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
