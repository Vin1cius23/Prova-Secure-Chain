#!/bin/bash

DATA=$(date +%Y-%m-%d_%H-%M-%S)
ARQ="backup/documentos_$DATA.tar.gz"
CRIPTO="backup/documentos_$DATA.tar.gz.enc"
SENHA="123456"

tar -czf "$ARQ" documentos

openssl enc -aes-256-cbc -pbkdf2 -salt -in "$ARQ" -out "$CRIPTO" -pass pass:$SENHA

if [ $? -eq 0 ]; then
    TAMANHO=$(du -h "$CRIPTO" | cut -f1)
    echo "$DATA | Backup OK | $CRIPTO | $TAMANHO" >> logs/backup.log
    python3 -c "from blockchain.blockchain import novo_evento; novo_evento('Backup criptografado executado')"
    echo "Backup criptografado criado: $CRIPTO"
else
    echo "$DATA | Backup FALHOU" >> logs/backup.log
    echo "Erro no backup"
fi
