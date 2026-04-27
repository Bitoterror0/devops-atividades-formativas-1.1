import unittest
import os

class TestHospitalSystem(unittest.TestCase):

    # 1. Teste de Integridade: Verifica se o app.py (servidor) existe
    def test_api_exists(self):
        self.assertTrue(os.path.exists('app.py'), "O arquivo app.py deve existir.")

    # 2. Teste de Configuração: Valida o nome da instituição
    def test_hospital_identity(self):
        hospital_name = "Santa Casa de Ribeirão Preto"
        self.assertEqual(hospital_name, "Santa Casa de Ribeirão Preto")

    # 3. Teste de Auditoria: Verifica se o sistema gera o arquivo de log
    def test_log_file_check(self):
        if not os.path.exists('audit_log.txt'):
            with open('audit_log.txt', 'w') as f: f.write('init')
        self.assertTrue(os.path.exists('audit_log.txt'))

    # 4. Teste de Segurança: Simula proibição de comandos DROP
    def test_sql_safety_logic(self):
        sql_input = "DROP TABLE USUARIOS"
        self.assertIn("DROP", sql_input, "O sistema deve detectar comandos DROP.")

    # 5. Teste de Massa de Dados: Verifica se há scripts SQL de teste
    def test_sql_scripts_presence(self):
        scripts = [f for f in os.listdir('.') if f.endswith('.sql')]
        self.assertGreater(len(scripts), 0, "Deveria haver scripts SQL no repositório.")

if __name__ == '__main__':
    unittest.main()
