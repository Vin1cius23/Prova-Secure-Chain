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
## Medidas de Segurança

- Senhas armazenadas utilizando hash SHA-256.
- Integridade dos arquivos verificada por hash criptográfico.
- Eventos registrados em blockchain imutável.
- Backups protegidos por criptografia AES-256.
- Aplicação do princípio do menor privilégio através de permissões Linux.
## Blockchain de Auditoria

Cada evento gera um novo bloco contendo:

- ID do bloco
- Timestamp
- Descrição do evento
- Hash do bloco anterior
- Hash atual do bloco

A integridade da cadeia pode ser validada através da função de validação da blockchain.
## Monitoramento de Integridade

O sistema monitora o diretório `documentos/` utilizando hashes SHA-256.

Eventos detectados:

- Criação de arquivos
- Alteração de arquivos
- Exclusão de arquivos

Toda alteração gera automaticamente um registro na blockchain de auditoria.
## Backup Seguro

O sistema realiza backup dos documentos monitorados através de:

1. Compactação em formato `.tar.gz`
2. Criptografia utilizando AES-256 via OpenSSL
3. Registro automático do evento na blockchain
4. Armazenamento de logs da operação

Essa abordagem garante confidencialidade e rastreabilidade dos backups.
