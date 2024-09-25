import random
import pandas as pd
from faker import Faker

# Gerar dados
fake = Faker('pt_BR')

num_registros = 10
dados = []

while len(dados) < num_registros-1:
    nome = fake.name()
    cpf = fake.unique.cpf()
    matricula = fake.unique.random_number(digits=15)
    email = fake.unique.email()
    
    codigo_setor = random.randint(1, 1)
    if codigo_setor == 1:
        codigo_cargo = random.choice([1, 1])
    else:
        codigo_cargo = random.choice([1, 1])
    
    data_admissao = fake.date_object().strftime('%d/%m/%Y')
    gestor = random.randint(0, 1)
    
    dados.append([nome, cpf, matricula, email, codigo_setor, codigo_cargo, data_admissao, gestor])

# Criar DataFrame e salvar como CSV
colunas = ["NOME", "CPF", "MATRICULA", "EMAIL", "CODIGO DO SETOR", "CODIGO DO CARGO", "DATA DE ADMISSAO", "GESTOR"]
df_novo = pd.DataFrame(dados, columns=colunas)

# Salvar em um novo arquivo CSV
novo_arquivo_path = 'massa_de_dados_validos.csv'
df_novo.to_csv(novo_arquivo_path, index=False)