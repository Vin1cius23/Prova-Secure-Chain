from blockchain.blockchain import novo_evento
import hashlib
import json
import os

ARQ = "usuarios/users.json"

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar():
    if not os.path.exists(ARQ):
        return {}
    with open(ARQ) as f:
        return json.load(f)

def salvar(dados):
    with open(ARQ, "w") as f:
        json.dump(dados, f, indent=4)

def cadastrar():
    user = input("Novo usuario: ")
    senha = input("Nova senha: ")

    dados = carregar()

    if user in dados:
        print("Usuario já existe")
        return

    dados[user] = hash_senha(senha)
    salvar(dados)
    print("Usuario criado!")

def login():
    user = input("Usuario: ")
    senha = input("Senha: ")

    dados = carregar()

    if dados.get(user) == hash_senha(senha):
        print("Login OK")
        novo_evento(f"Login realizado: {user}")
        return True, user
    else:
        print("Login inválido")
        novo_evento(f"Falha no login: {user}")
        return False, user
if __name__ == "__main__":
    print("1 - Cadastrar")
    print("2 - Login")

    op = input("Escolha: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        login()

