import pandas as pd
import chardet

def collect_from_csv(file_path="data/raw/raw_data.csv"):
    """
    Coleta dados de um arquivo CSV.
    
    Args:
    - file_path (str): Caminho para o arquivo CSV.
    
    Returns:
    - DataFrame: Dados coletados.
    """
    try:
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        
        data = pd.read_csv(file_path, encoding=result['encoding'])
        print(f"Dados sendo coletados com sucesso. Aguarde! de {file_path}")
        return data
    except Exception as e:
        print(f"Erro ao coletar dados do arquivo CSV: {e}")
        return None


def preprocess_data(data):
    """
    Realiza pré-processamento básico nos dados.
    
    Args:
    - data (DataFrame): Dados brutos.
    
    Returns:
    - DataFrame: Dados pré-processados.
    """
    # Remove duplicatas
    data.drop_duplicates(inplace=True)
    
    # Preenchendo valores ausentes
    for column in data.columns:
        if data[column].dtype == 'O':  # Se a coluna for categórica
            data[column].fillna(data[column].mode()[0], inplace=True)
        else:
            data[column].fillna(data[column].median(), inplace=True)
    
    # Remove colunas com mais de 70% de valores ausentes
    threshold = 0.7 * len(data)
    data.dropna(axis=1, thresh=threshold, inplace=True)
    
    # Codificação one-hot para colunas categóricas
    data = pd.get_dummies(data, drop_first=True)
    
    return data

def collect_data():
    print("Iniciando coleta de dados...")
    
    # Coleta de dados de um arquivo CSV
    data = collect_from_csv()
    
    # Verificar se os dados não são None antes de prosseguir
    if data is not None:
        # Pré-processamento dos dados
        data = preprocess_data(data)
    
    return data

if __name__ == "__main__":
    collect_data()

