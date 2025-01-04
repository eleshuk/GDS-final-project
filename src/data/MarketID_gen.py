import pandas as pd
import os

# Caminhos
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\MarketData.xlsx"
output_path = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket"
output_file = os.path.join(output_path, "MarketData_with_ids.xlsx")

# Carregar o arquivo Excel
df = pd.read_excel(input_file)

# Gerar identificadores hierárquicos
# Formato: SOIL-001, SOIL-002, ...
df['MarketID'] = ['MRKT-' + str(i).zfill(3) for i in range(1, len(df) + 1)]

# Salvar o novo arquivo Excel
df.to_excel(output_file, index=False)

print(f"Arquivo salvo com sucesso em: {output_file}")