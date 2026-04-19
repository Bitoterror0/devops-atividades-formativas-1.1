import os
import sys

def validar_scripts():
    print("--- SCANNER DE SEGURANÇA SQL ---")
    
    # Comandos que não podem estar nos scripts de deploy comum
    comandos_perigosos = ["DROP TABLE", "DROP DATABASE", "TRUNCATE"]
    erros = 0

    sql_files = [f for f in os.listdir('.') if f.endswith('.sql')]

    for file in sql_files:
        with open(file, 'r', encoding='utf-8') as f:
            conteudo = f.read().upper()
            for comando in comandos_perigosos:
                if comando in conteudo:
                    print(f"❌ ALERTA DE SEGURANÇA: Comando '{comando}' detectado no arquivo {file}!")
                    erros += 1
            
            # Validação extra: DELETE sem WHERE
            if "DELETE" in conteudo and "WHERE" not in conteudo:
                print(f" ALERTA CRÍTICO: Comando 'DELETE' sem 'WHERE' no arquivo {file}!")
                erros += 1

    if erros > 0:
        print(f"\n--- VALIDAÇÃO FALHOU: {erros} FALHAS ENCONTRADAS ---")
        sys.exit(1) # Faz o Docker e o GitHub Actions pararem aqui
    else:
        print("\n--- NENHUMA FALHA DE SEGURANÇA ENCONTRADA ---")
        sys.exit(0)

if __name__ == "__main__":
    validar_scripts()
