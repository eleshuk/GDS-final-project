import pandas as pd

# Caminhos
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\processed\region_f.csv"
output_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\processed\region_f_with.csv"

try:
    # Carregar o arquivo CSV com UTF-8-SIG para remover o BOM
    df = pd.read_csv(input_file, encoding='utf-8-sig', delimiter=';')
except FileNotFoundError:
    print(f"Erro: O ficheiro '{input_file}' não foi encontrado. Verifica o caminho.")
    raise
except pd.errors.ParserError as e:
    print(f"Erro ao processar o arquivo CSV: {e}")
    raise

# Exibir as colunas para verificar se foram carregadas corretamente
print("Colunas disponíveis no arquivo:", df.columns.tolist())

# Verificar se a coluna 'district' está presente
if 'district' not in df.columns:
    raise ValueError("A coluna 'district' não está presente no arquivo. Verifica os nomes das colunas.")

# Criar a coluna DesertificationRisk com base na lista de distritos
susceptible_districts = [
    "Beja", "Évora", "Setúbal", "Faro", "Portalegre", "Santarém", "Castelo Branco"
]

# Adicionar classificação com base nos distritos
df['DesertificationRisk'] = df['district'].apply(
    lambda x: 'susceptível' if x in susceptible_districts else 'não susceptível'
)

# Salvar o arquivo atualizado
try:
    df.to_csv(output_file, index=False, sep=';', encoding='latin1')
    print(f"Arquivo salvo com sucesso em: {output_file}")
except Exception as e:
    print(f"Erro ao salvar o ficheiro: {e}")
    raise
