import os
from datetime import datetime
from blockchain.blockchain import novo_evento

def gerar_relatorio():

    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    arquivo = f"auditoria/relatorios/relatorio_{data}.txt"

    with open(arquivo, "w") as f:

        f.write("===== WHO =====\n")
        f.write(os.popen("who").read())

        f.write("\n\n===== LAST =====\n")
        f.write(os.popen("last").read())

        f.write("\n\n===== SS =====\n")
        f.write(os.popen("ss -tulpn").read())

        f.write("\n\n===== IP A =====\n")
        f.write(os.popen("ip a").read())

    novo_evento("Relatorio de auditoria gerado")

    print(f"Relatório criado: {arquivo}")

if __name__ == "__main__":
    gerar_relatorio()
