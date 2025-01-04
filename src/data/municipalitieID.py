import pandas as pd
import os

# Caminho do arquivo de entrada
input_path = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\processed\Region.csv"

# Caminho do diretório de saída
output_dir = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\processed"

# Lê o arquivo CSV com ponto e vírgula como separador
df = pd.read_csv(input_path, sep=';', quotechar='"', escapechar='\\')

# Cria um dicionário com os municípios e seus índices
municipios = {municipio: index + 1 for index, municipio in enumerate(df['municipality'].unique())}

# Função para criar a chave primária da municipalidade
def criar_municipalidade_id(row):
    return f"MUN-{row['region_id']}-{municipios[row['municipality']]:03d}"

# Aplica a função para criar a nova coluna
df['municipalidade_id'] = df.apply(criar_municipalidade_id, axis=1)

# Cria o caminho completo para o arquivo de saída
output_path = os.path.join(output_dir, 'Region_updated.csv')

# Salva o DataFrame atualizado em um novo arquivo CSV
df.to_csv(output_path, index=False, sep=';')

print(f"Arquivo atualizado salvo como '{output_path}'")
