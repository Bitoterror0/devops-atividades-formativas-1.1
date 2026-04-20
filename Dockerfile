# Imagem base leve (Padrão de mercado para eficiência)
FROM alpine:latest

# Define o diretório de trabalho
WORKDIR /app

# Instala Python e o Flask (Transformando o container em um Servidor Web/API)
# Usamos o --break-system-packages para permitir a instalação do pip no ambiente Alpine atual
RUN apk add --no-cache python3 py3-pip && \
    pip install flask --break-system-packages

# Copia todos os arquivos (Scripts SQL, Auditoria, Segurança, Massa de Dados e a nova API)
COPY . . 

# --- CAMADAS DE AUTOMAÇÃO NO BUILD ---
# Validação de Segurança (DevSecOps)
RUN python3 validador_seguranca.py

# Geração de massa de dados para o Banco de Dados Hospitalar
RUN python3 gerador_massa_dados.py

# --- HISTÓRICO DE EVOLUÇÃO (COMANDOS ANTERIORES) ---
# CMD ["main.py""sh", "-c", "ls -R && python3 --version"]
# CMD ["python3", "main.py"]
# CMD python3 main.py && cat audit_log.txt
# CMD ["sh", "-c", "python3 main.py && cat audit_log.txt"]
# CMD ["sh", "-c", "python3 main.py && python3 dashboard_saude.py"]

# --- O TOQUE DE GÊNIO: MODO MICROSERVIÇO ---
# Informa que o container escuta na porta 5000 (Padrão de APIs Flask)
EXPOSE 5000

# O comando final agora mantém o servidor vivo e executa a auditoria no início
CMD ["sh", "-c", "python3 main.py && python3 app.py"]
