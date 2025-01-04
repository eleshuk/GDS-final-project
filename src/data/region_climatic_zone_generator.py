import pandas as pd

# Caminhos dos ficheiros
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\processed\region_f.csv"
output_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\processed\region_f_with_climate.csv"

try:
    # Carregar o ficheiro CSV
    df = pd.read_csv(input_file, encoding='latin1', delimiter=';')
except FileNotFoundError:
    print(f"Erro: O ficheiro '{input_file}' não foi encontrado. Verifica o caminho.")
    raise
except UnicodeDecodeError as e:
    print(f"Erro de codificação ao processar o ficheiro: {e}")
    raise

# Exibir as colunas para verificar se foram carregadas corretamente
print("Colunas disponíveis no ficheiro:", df.columns.tolist())

# Verificar se a coluna 'municipality' está presente
if 'municipality' not in df.columns:
    raise ValueError("A coluna 'municipality' não está presente no ficheiro. Verifica os nomes das colunas.")

# Lista de municípios por zona climática
climate_csa = [
    # Municípios exclusivamente na zona Csa (quente)
    "Aljustrel", "Almodôvar", "Alvito", "Barrancos", "Beja", "Castro Verde", "Cuba",
    "Ferreira do Alentejo", "Mértola", "Moura", "Odemira", "Ourique", "Serpa", "Vidigueira",
    "Alandroal", "Arraiolos", "Borba", "Estremoz", "Évora", "Montemor-o-Novo", "Mourão",
    "Portel", "Redondo", "Reguengos de Monsaraz", "Vendas Novas", "Vila Viçosa",
    "Albufeira", "Alcoutim", "Aljezur", "Castro Marim", "Faro", "Lagoa", "Lagos",
    "Loulé", "Monchique", "Olhão", "Portimão", "São Brás de Alportel", "Silves", "Tavira", "Vila do Bispo"
]

climate_csb = [
    # Municípios exclusivamente na zona Csb (pouco quente)
    "Águeda", "Albergaria-a-Velha", "Anadia", "Arouca", "Aveiro", "Castelo de Paiva", "Espinho",
    "Estarreja", "Ílhavo", "Mealhada", "Murtosa", "Oliveira de Azeméis", "Oliveira do Bairro",
    "Ovar", "São João da Madeira", "Sever do Vouga", "Vagos", "Vale de Cambra",
    "Amares", "Barcelos", "Braga", "Cabeceiras de Basto", "Celorico de Basto", "Esposende",
    "Fafe", "Guimarães", "Póvoa de Lanhoso", "Terras de Bouro", "Vieira do Minho", "Vila Nova de Famalicão",
    "Vila Verde", "Vizela", "Arcos de Valdevez", "Caminha", "Melgaço", "Monção",
    "Paredes de Coura", "Ponte da Barca", "Ponte de Lima", "Valença", "Viana do Castelo", "Vila Nova de Cerveira"
]

climate_mixed = [
    # Municípios em zona Mista (Csa/Csb)
    "Portalegre", "Marvão", "Castelo Branco", "Idanha-a-Nova", "Guarda", "Seia", "Manteigas", 
    "Vila Real", "Sabugal", "Trancoso", "Gouveia"
]

# Função para classificar o clima
def classify_climate(municipality):
    if municipality in climate_csa:
        return "Csa"  # Quente
    elif municipality in climate_csb:
        return "Csb"  # Pouco quente
    elif municipality in climate_mixed:
        return "Misto"  # Ambas as zonas
    else:
        return "Desconhecido"  # Não categorizado

# Adicionar a coluna ClimateZone
df['ClimateZone'] = df['municipality'].apply(classify_climate)

# Identificar municípios que não foram classificados
not_classified = df[df['ClimateZone'] == "Desconhecido"]

# Salvar o ficheiro atualizado
try:
    df.to_csv(output_file, index=False, sep=';', encoding='utf-8-sig')
    print(f"Ficheiro salvo com sucesso em: {output_file}")
    
    # Exibir municípios não classificados
    if not not_classified.empty:
        print("\nATENÇÃO: Existem municípios não classificados:")
        print(not_classified[['municipality']])
    else:
        print("\nTodos os municípios foram classificados com sucesso.")
except Exception as e:
    print(f"Erro ao salvar o ficheiro: {e}")
    raise
