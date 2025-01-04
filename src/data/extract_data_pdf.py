import pdfplumber
import pandas as pd

# Caminho para o PDF
pdf_path = r"C:\Users\Luís Pinto Coelho\Downloads\MAF1951-1980_RelatorioTecnico.pdf"
output_csv_path = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\extracted_data.csv"

# Lista para armazenar os dados extraídos
data = []

# Função para limpar caracteres estranhos
def clean_text(text):
    if isinstance(text, str):
        return text.encode('latin1', errors='ignore').decode('utf-8', errors='ignore').strip()
    return text

with pdfplumber.open(pdf_path) as pdf:
    # Iterar sobre as páginas do PDF
    for page in pdf.pages:
        # Extrair tabelas
        tables = page.extract_tables()
        for table in tables:
            # Adicionar todas as linhas da tabela aos dados
            for row in table:
                data.append([clean_text(cell) for cell in row])  # Limpar cada célula

# Verificar se há dados extraídos
if data:
    # Assumir o cabeçalho com base nos dados fornecidos
    columns = ["MAF5180Cod", "MAF5180Ori", "MAF5180Leg", "COSn1", "COSn2", "COSn3", "COSn4"]
    
    # Garantir que o número de colunas está correto
    filtered_data = [row for row in data if len(row) == len(columns)]
    
    # Criar DataFrame
    df = pd.DataFrame(filtered_data, columns=columns)
    
    # Salvar o DataFrame como CSV
    df.to_csv(output_csv_path, index=False, encoding="utf-8-sig", sep=",")
    print(f"Dados extraídos e salvos em {output_csv_path}")
else:
    print("Nenhuma tabela foi encontrada no PDF.")
