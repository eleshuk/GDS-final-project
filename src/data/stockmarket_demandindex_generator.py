import pandas as pd
import random
import numpy as np

# Caminhos dos ficheiros
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\MarketData.xlsx"
output_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\MarketData_with_DemandIndex.xlsx"

# Função para normalizar valores entre 0 e 1
def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

# Função para gerar DemandIndex ajustado
def generate_demand_index(price_per_ton, price_min, price_max):
    # Normalizar PricePerTon
    normalized_price = normalize(price_per_ton, price_min, price_max)
    
    # Aplicar fórmula ajustada
    factor = 0.8  # Controla o peso da relação inversa
    demand_index = 1 - (normalized_price * factor) + random.uniform(-0.3, 0.3)  # Adiciona variação equilibrada
    demand_index = max(0, min(demand_index, 1))  # Garante que o valor esteja entre 0 e 1
    return round(demand_index, 2)  # Arredonda para duas casas decimais

# Carregar o ficheiro de entrada
df = pd.read_excel(input_file)

# Determinar os valores mínimos e máximos de PricePerTon
price_min = df["PricePerTon"].min()
price_max = df["PricePerTon"].max()

# Gerar dados para DemandIndex
df["DemandIndex"] = df["PricePerTon"].apply(lambda price: generate_demand_index(price, price_min, price_max))

# Salvar o ficheiro de saída
df.to_excel(output_file, index=False)

print(f"Dados gerados e salvos em: {output_file}")