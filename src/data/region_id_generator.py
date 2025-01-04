import pandas as pd

# Caminhos para carregar e salvar o ficheiro
input_path = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\Region.csv"
output_path = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\Region\Region_with_ids.csv"

try:
    # Carregar o CSV e especificar o delimitador correto
    df = pd.read_csv(input_path, encoding='latin1', delimiter=',', on_bad_lines='skip')  
    
    # Verificar se o arquivo foi carregado corretamente
    print(f"Ficheiro carregado com {len(df)} linhas e {len(df.columns)} colunas.")
    
    # Adicionar a coluna 'region_id' com IDs únicos
    df['region_id'] = range(1, len(df) + 1)
    
    # Reordenar as colunas para que 'region_id' venha primeiro
    columns_order = ['region_id'] + [col for col in df.columns if col != 'region_id']
    df = df[columns_order]
    
    # Salvar o novo ficheiro CSV, garantindo o delimitador correto
    df.to_csv(output_path, index=False, encoding='latin1', sep=',')
    print(f"Novo ficheiro salvo com sucesso em: {output_path}")

except FileNotFoundError:
    print(f"Erro: O ficheiro '{input_path}' não foi encontrado.")
except PermissionError:
    print(f"Erro: Sem permissão para salvar o ficheiro em '{output_path}'.")
except pd.errors.ParserError as e:
    print(f"Erro ao processar o CSV: {e}")
    print("Verifique o formato do arquivo e o delimitador usado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
