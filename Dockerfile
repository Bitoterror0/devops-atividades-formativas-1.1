# Imagem base leve
FROM alpine:latest
# Define o diretório dentro do container
WORKDIR /app
# Copia scripts SQL e o README para o container
COPY . . 
# Comando apenas para validar que os arquivos estão lá
CMD ["ls", "-R"]
