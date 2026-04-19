# 1. Começa com a sua imagem leve
FROM alpine:latest
# 2. Define o diretório
WORKDIR /app
# 3. INSTALA O PYTHON (A mágica acontece aqui)
# O apk é o instalador do Alpine (tipo o apt-get do Ubuntu)
RUN apk add --no-update python3 py3-pip
# 4. Copia seus arquivos (SQL, README e agora seus .py)
COPY . .
# 5. Valida os arquivos e a versão do Python
CMD ["sh", "-c", "ls -R && python3 --version"]
