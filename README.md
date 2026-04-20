# devops-atividades-formativas-1.1
Atividade PUCPR

Hospital DevOps Pipeline & API
Este repositório contém uma solução completa de Infraestrutura como Código (IaC) e Automação de Dados voltada para o setor hospitalar. O projeto integra scripts de banco de dados SQL com uma camada de automação em Python, tudo empacotado em um container Docker escalável.
 Funcionalidades do Projeto
O pipeline foi desenhado para seguir os pilares de DevSecOps e SRE (Site Reliability Engineering):
1.	Segurança (DevSecOps): O script validador_seguranca.py analisa todos os arquivos .sql em busca de comandos perigosos (DROP, TRUNCATE) ou DELETE sem WHERE antes do build ser concluído.
2.	Engenharia de Dados: O gerador_massa_dados.py cria automaticamente massa de dados sintéticos para testes, garantindo conformidade com a LGPD ao evitar o uso de dados reais de pacientes.
3.	Auditoria Automatizada: O main.py realiza o mapeamento de todos os artefatos de banco de dados e gera um log de auditoria (audit_log.txt).
4.	Monitoramento (BI): O dashboard_saude.py gera uma telemetria visual no console sobre o estado da infraestrutura.
5.	Microserviço (API): Uma API Flask (app.py) expõe o status do sistema via JSON na porta 5000.
________________________________________
 Tecnologias Utilizadas
•	Docker: Conteinerização e portabilidade.
•	Python 3: Lógica de automação, segurança e API.
•	Flask: Framework para o microserviço web.
•	SQL: Estrutura de banco de dados hospitalar.
•	GitHub Actions: Pipeline de CI/CD para automação de builds e testes.
________________________________________
 Como Executar o Projeto
Pré-requisitos
•	Docker instalado localmente.
Passo 1: Construir a Imagem
No terminal, dentro da pasta do projeto, execute:
PowerShell
docker build -t hospital-devops-api .
Passo 2: Rodar o Container
Para acessar a API e ver o dashboard, mapeie a porta 5000:
PowerShell
docker run -p 5000:5000 hospital-devops-api
Passo 3: Acessar a API
Abra o seu navegador e acesse: http://localhost:5000
________________________________________
 Estrutura de Arquivos
•	Dockerfile: Receita de construção da imagem Alpine Linux.
•	app.py: Servidor Flask que expõe o Health Check do sistema.
•	validador_seguranca.py: Filtro de segurança para scripts SQL.
•	gerador_massa_dados.py: Gerador de inserts aleatórios de pacientes.
•	main.py: Script principal de auditoria.
•	dashboard_saude.py: Telemetria e resumo executivo do sistema.
•	*.sql: Scripts de estrutura e dados do banco hospitalar.
________________________________________
 Camada de Segurança
O projeto utiliza um Quality Gate no Dockerfile. Se qualquer script SQL violar as regras de segurança, o comando RUN python3 validador_seguranca.py retornará erro, impedindo que uma imagem insegura seja gerada ou enviada para produção.
________________________________________
Autor
Victor Silva Lopes Analista de Sistemas 
