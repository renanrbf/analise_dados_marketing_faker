# Importando as bibliotecas necessárias
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# --- Configurações Iniciais ---
NUM_SESSOES = 10000
TAXA_CONVERSAO_A_CARRINHO = 0.13 # 13%
TAXA_CONVERSAO_B_CARRINHO = 0.18 # 18% -> Nossa hipótese é que B é melhor
TAXA_CONVERSAO_FINAL_APOS_CARRINHO = 0.40 # 40% de quem adiciona ao carrinho, compra
DATA_INICIAL = datetime(2025, 7, 1)
DATA_FINAL = datetime(2025, 8, 12)

# Garantir a reprodutibilidade dos dados
Faker.seed(42)
random.seed(42)
fake = Faker('pt_BR')

# --- Geração dos Dados ---

dados_sessoes = []

for i in range(NUM_SESSOES):
    
    # 1. Atribuição ao grupo de teste A/B
    grupo = random.choice(['Layout_A', 'Layout_B'])
    
    # 2. Simulação da conversão (adição ao carrinho) com base no grupo
    if grupo == 'Layout_A':
        adicionou_ao_carrinho = random.random() < TAXA_CONVERSAO_A_CARRINHO
    else:
        adicionou_ao_carrinho = random.random() < TAXA_CONVERSAO_B_CARRINHO
        
    # 3. Simulação da compra (só pode comprar se adicionou ao carrinho)
    comprou = False
    valor_compra = 0
    if adicionou_ao_carrinho:
        if random.random() < TAXA_CONVERSAO_FINAL_APOS_CARRINHO:
            comprou = True
            valor_compra = round(random.uniform(50.0, 650.0), 2)
            
    # 4. Geração de dados demográficos e de sessão
    user_id = fake.uuid4()
    timestamp_visita = fake.date_time_between(start_date=DATA_INICIAL, end_date=DATA_FINAL)
    tempo_na_pagina = random.randint(15, 300) # em segundos
    
    # 5. Geração de dados de aquisição para cálculo de ROI
    canal_aquisicao = random.choices(['Organico', 'CPC', 'Social'], weights=[0.5, 0.3, 0.2], k=1)[0]
    custo_clique = 0
    if canal_aquisicao == 'CPC':
        custo_clique = round(random.uniform(0.75, 3.50), 2)
        
    # 6. Montagem do dicionário da sessão
    dados_sessoes.append({
        'session_id': fake.uuid4(),
        'user_id': user_id,
        'timestamp_visita': timestamp_visita,
        'pagina_visitada': grupo,
        'tempo_na_pagina_segundos': tempo_na_pagina,
        'canal_aquisicao': canal_aquisicao,
        'custo_clique': custo_clique,
        'adicionou_ao_carrinho': adicionou_ao_carrinho,
        'comprou': comprou,
        'valor_compra': valor_compra
    })

# --- Criação e Salvamento do DataFrame ---

# Converter a lista de dicionários em um DataFrame do Pandas
df_ecommerce = pd.DataFrame(dados_sessoes)

# Caminho para salvar o arquivo na pasta 'data'
caminho_arquivo = os.path.join('data', 'dados_ecommerce.csv')

# Salvar o DataFrame no formato CSV
df_ecommerce.to_csv(caminho_arquivo, index=False)

print(f"Arquivo '{caminho_arquivo}' gerado com sucesso!")
print(f"Total de {len(df_ecommerce)} sessões criadas.")
print("\nVisualização das 5 primeiras linhas:")
print(df_ecommerce.head())