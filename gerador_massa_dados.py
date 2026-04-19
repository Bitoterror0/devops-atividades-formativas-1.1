import random

def gerar_cpf():
    return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"

def gerar_massa_dados(quantidade=10):
    nomes = ["Victor", "Benhur", "Adriana", "Marcos", "Beatriz", "Ricardo", "Juliana", "Fernando"]
    sobrenomes = ["Silva", "Lopes", "Oliveira", "Santos", "Costa", "Pereira", "Souza"]
    
    filename = "carga_pacientes_teste.sql"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("-- ARQUIVO GERADO AUTOMATICAMENTE PARA TESTE DE CARGA --\n")
        f.write("INSERT INTO PACIENTES (NOME, CPF, DATA_CADASTRO) VALUES\n")
        
        for i in range(quantidade):
            nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
            cpf = gerar_cpf()
            virgula = "," if i < quantidade - 1 else ";"
            f.write(f"('{nome_completo}', '{cpf}', CURRENT_TIMESTAMP){virgula}\n")
            
    print(f"--- ✅ SUCESSO: {quantidade} REGISTROS GERADOS EM {filename} ---")

if __name__ == "__main__":
    gerar_massa_dados(15) # Gerar 15 para testar
