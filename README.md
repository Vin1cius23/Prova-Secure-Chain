# SecureChain Audit

Plataforma de auditoria baseada em blockchain, desenvolvida em Debian com Python e Bash.

## Funcionalidades

- Controle de usuários
- Autenticação com senha em hash SHA-256
- Blockchain para registro de eventos
- Monitoramento de integridade de arquivos
- Backup compactado e criptografado com AES-256
- Auditoria do sistema operacional
- Validação da integridade da blockchain

## Estrutura

```text
securechain/
├── blockchain/
│   ├── blockchain.py
│   └── chain.json
├── auditoria/
│   ├── auditor.py
│   └── relatorios/
├── backup/
│   └── backup.sh
├── documentos/
├── logs/
├── usuarios/
├── auth.py
├── monitor.py
└── README.md
## Fluxo de Auditoria

1. O usuário realiza login no sistema.
2. O evento é registrado na blockchain.
3. Os arquivos do diretório documentos são monitorados.
4. Alterações geram novos blocos na blockchain.
5. Backups criptografados são registrados na cadeia.
6. Relatórios de auditoria são gerados automaticamente.
