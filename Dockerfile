# Imagem base leve
FROM alpine:latest

# Define o diretório dentro do container
WORKDIR /app

# Instala o Python 3 de forma limpa
RUN apk add --no-cache python3

# Copia todos os arquivos (Scripts SQL, README e Scripts Python)
COPY . . 

# Roda o validador de segurança. 
# Se ele der erro (sys.exit(1)), o build do GitHub Actions para aqui.
RUN python3 validador_seguranca.py

# Gera a massa de dados automática para testes
RUN python3 gerador_massa_dados.py

# --- SEÇÃO DE COMANDOS ANTERIORES (HISTÓRICO) ---
# CMD ["main.py""sh", "-c", "ls -R && python3 --version"]
# CMD ["python3", "main.py"]
# CMD python3 main.py && cat audit_log.txt
# CMD ["sh", "-c", "python3 main.py && cat audit_log.txt"]

# --- CEREJA DO BOLO: EXECUÇÃO FINAL ---
# Roda a auditoria e exibe o Dashboard de Monitoramento Hospitalar
CMD ["sh", "-c", "python3 main.py && python3 dashboard_saude.py"]
