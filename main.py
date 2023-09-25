import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

from scripts.data_collection import collect_data
from src.data_preprocessing import DataPreprocessor
from scripts.train_model import train_model, load_model, save_model, predict

# Definindo as colunas diretamente no código
config = {
    'categorical_columns': [
        'Marca',
        'Modelo',
        'Combustivel',
        'Tracao',
        'Litros',
        'Valvulas',
        'Cambio',
        'Inducao',
        'Versao'
    ]
}

def main(args):
    if args.collect_data:
        data = collect_data()
        data.to_csv('data/raw/raw_data.csv', index=False)
        print("Dados coletados com sucesso!")

    if args.preprocess:
        # Lendo os dados brutos
        data = pd.read_csv('data/raw/raw_data.csv')  
        preprocessor = DataPreprocessor(config)
        processed_data = preprocessor.preprocess(data)
        processed_data.to_csv('data/processed/processed_data.csv', index=False)
        print("Dados pré-processados com sucesso!")
    

    if args.train:
        data = pd.read_csv('data/processed/processed_data.csv')
        # Verifique se a coluna "Preço Médio" existe, caso contrário, use "Preco Medio"
        target_column = 'Preço Médio' if 'Preço Médio' in data.columns else 'Preco Medio'
        
        X_train, X_test, y_train, y_test = train_test_split(data.drop(target_column, axis=1), data[target_column], test_size=0.2)
        model = train_model(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Modelo treinado com sucesso! MSE: {mse}")
        save_model(model, 'trained_model.pkl')
    

    if args.predict:
          # Carregue o modelo treinado
      try:
          model = load_model('trained_model.pkl')
          print("Modelo carregado com sucesso.")
      except Exception as e:
          print(f"Erro ao carregar o modelo: {e}")
          return
  
      # Carregue o preprocessador salvo
      try:
          preprocessor = joblib.load('preprocessor.pkl')
          print("Preprocessador carregado com sucesso.")
      except FileNotFoundError:
          print("Erro: O preprocessador não foi encontrado. Certifique-se de treinar o modelo primeiro.")
          return
      except Exception as e:
          print(f"Erro ao carregar o preprocessador: {e}")
          return
  
      # Carregue os dados de amostra
      try:
          sample_data = pd.read_csv('data/processed/sample_data.csv')
          print("Dados de amostra carregados com sucesso.")
      except FileNotFoundError:
          print("Erro: Dados de amostra não encontrados.")
          return
      except Exception as e:
          print(f"Erro ao carregar dados de amostra: {e}")
          return
  
      # Pré-processar os dados de amostra usando o preprocessador carregado
      try:
          processed_sample_data = preprocessor.preprocess(sample_data, is_training=False)
          print("Dados de amostra pré-processados com sucesso.")
      except Exception as e:
          print(f"Erro ao pré-processar dados de amostra: {e}")
          return
  
      # Remova a coluna "Preco Medio" dos dados processados antes de fazer a previsão
      if 'Preco Medio' in processed_sample_data.columns:
          processed_sample_data.drop('Preco Medio', axis=1, inplace=True)
  
      # Faça previsões usando o modelo
      try:
          predictions = predict(model, processed_sample_data)
          print(f"Previsões: {predictions}")
      except Exception as e:
          print(f"Erro ao fazer previsões: {e}")
          return
  
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script principal para operacionalizar o projeto de data science.")
    parser.add_argument('--collect_data', action='store_true', help="Coleta de dados.")
    parser.add_argument('--preprocess', action='store_true', help="Pré-processamento dos dados.")
    parser.add_argument('--train', action='store_true', help="Treinamento do modelo.")
    parser.add_argument('--predict', action='store_true', help="Realizar previsões com o modelo treinado.")
    
    args = parser.parse_args()
    main(args)
