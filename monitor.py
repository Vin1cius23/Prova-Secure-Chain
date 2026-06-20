import hashlib
import os
import json
from blockchain.blockchain import novo_evento

PASTA = "documentos"
ARQ_HASHES = "hashes.json"

def hash_arquivo(caminho):
    with open(caminho, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def gerar_base():
    hashes = {}

    for nome in os.listdir(PASTA):
        caminho = os.path.join(PASTA, nome)
        if os.path.isfile(caminho):
            hashes[nome] = hash_arquivo(caminho)

    with open(ARQ_HASHES, "w") as f:
        json.dump(hashes, f, indent=4)

    print("Base de hashes criada.")

def verificar():
    if not os.path.exists(ARQ_HASHES):
        gerar_base()
        return

    with open(ARQ_HASHES) as f:
        antigo = json.load(f)

    atual = {}

    for nome in os.listdir(PASTA):
        caminho = os.path.join(PASTA, nome)
        if os.path.isfile(caminho):
            atual[nome] = hash_arquivo(caminho)

    for nome in atual:
        if nome not in antigo:
            print("Arquivo criado:", nome)
            novo_evento(f"Arquivo criado: {nome}")
        elif atual[nome] != antigo[nome]:
            print("Arquivo alterado:", nome)
            novo_evento(f"Arquivo alterado: {nome}")

    for nome in antigo:
        if nome not in atual:
            print("Arquivo removido:", nome)
            novo_evento(f"Arquivo removido: {nome}")

    with open(ARQ_HASHES, "w") as f:
        json.dump(atual, f, indent=4)

if __name__ == "__main__":
    verificar()

