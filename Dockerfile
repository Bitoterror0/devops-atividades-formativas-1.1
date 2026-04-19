# Imagem base leve
FROM alpine:latest

# Define o diretório dentro do container
WORKDIR /app

# Instala o Python 3 de forma limpa
RUN apk add --no-cache python3
# Roda o validador de segurança. 
# Se ele der erro (sys.exit(1)), o container para aqui.
RUN python3 validador_seguranca.py

# Copia scripts SQL e o README para o container
COPY . . 

# Comando para validar arquivos e mostrar a versão do Python
#CMD ["main.py""sh", "-c", "ls -R && python3 --version"]
# Comando para rodar o script de validação Python
#CMD ["python3", "main.py"]
# Comando: Roda o Python e depois mostra o conteúdo do log gerado
CMD python3 main.py && cat audit_log.txt
