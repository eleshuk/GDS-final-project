import pandas as pd

# Caminho do arquivo de entrada e saída
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\soil_chart_pt.xlsx"
output_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\soil_chart_filled.xlsx"

# Mapeamento de Classes
class_mapping = {
    "Class 1": "Territórios artificializados",
    "Class 2": "Agricultura",
    "Class 3": "Pastagens",
    "Class 4": "Superfícies agroflorestais (SAF)",
    "Class 5": "Florestas",
    "Class 6": "Matos",
    "Class 7": "Espaços descobertos ou com pouca vegetação",
    "Class 8": "Zonas húmidas",
    "Class 9": "Massas de água superficiais"
}

# Carregar o arquivo Excel
df = pd.read_excel(input_file, engine='openpyxl')

# Preencher a nova coluna com base na coluna existente "Aptitude Class Level"
df['Aptitude_class_nomenclature'] = df['Aptitude Class Level'].map(class_mapping)

# Salvar o arquivo atualizado
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Arquivo salvo em: {output_file}")
