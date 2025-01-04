import pandas as pd
import os

# Caminhos
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Soil Type\processed\soil_unit.xlsx"
output_path = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Soil Type\processed"
output_file = os.path.join(output_path, "soil_unit_with_ids.xlsx")

# Carregar o arquivo Excel
df = pd.read_excel(input_file)

# Criar a coluna SoilUnit_id
# Formato: SU-001, SU-002, ...
df['SoilUnit_id'] = ['SU-' + str(i).zfill(3) for i in range(1, len(df) + 1)]

# Salvar o arquivo com a nova coluna
df.to_excel(output_file, index=False)

print(f"Arquivo salvo com sucesso em: {output_file}")
