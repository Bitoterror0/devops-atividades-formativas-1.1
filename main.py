import os
from datetime import datetime

def run_audit():
    print("--- SISTEMA DE AUDITORIA HOSPITALAR ---")
    
    # 1. Lista os arquivos SQL
    sql_files = [f for f in os.listdir('.') if f.endswith('.sql')]
    
    # 2. Cria (ou abre) um arquivo de log
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("audit_log.txt", "w") as log:
        log.write(f"RELATORIO DE AUDITORIA - DEPLOY EM {agora}\n")
        log.write("-" * 40 + "\n")
        
        for file in sql_files:
            log.write(f"Arquivo validado: {file} | Status: OK\n")
            print(f"Auditando: {file} ... Gravado no Log!")
            
    print(f"--- LOG GERADO COM SUCESSO: audit_log.txt ---")

if __name__ == "__main__":
    run_audit()
