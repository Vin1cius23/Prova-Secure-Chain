import hashlib
import json
from datetime import datetime

ARQ = "blockchain/chain.json"

def carregar():
    try:
        return json.load(open(ARQ))
    except:
        return []

def salvar(chain):
    json.dump(chain, open(ARQ, "w"), indent=4)

def gerar_hash(bloco):
    return hashlib.sha256(
        json.dumps(bloco, sort_keys=True).encode()
    ).hexdigest()

def novo_evento(evento):
    chain = carregar()

    bloco = {
        "id": len(chain),
        "timestamp": datetime.now().isoformat(),
        "evento": evento,
        "hash_anterior": chain[-1]["hash"] if chain else "0"
    }

    bloco["hash"] = gerar_hash(bloco)

    chain.append(bloco)
    salvar(chain)

def validar_chain():
    chain = carregar()

    for i in range(len(chain)):
        bloco = chain[i]

        hash_salvo = bloco["hash"]

        bloco_temp = bloco.copy()
        bloco_temp.pop("hash")

        hash_recalculado = gerar_hash(bloco_temp)

        if hash_recalculado != hash_salvo:
            print(f"ERRO: bloco {i} foi adulterado.")
            return False

        if i > 0:
            bloco_anterior = chain[i - 1]

            if bloco["hash_anterior"] != bloco_anterior["hash"]:
                print(f"ERRO: quebra de encadeamento no bloco {i}.")
                return False

    print("Blockchain íntegra.")
    return True

if __name__ == "__main__":
    validar_chain()
