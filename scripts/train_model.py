import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib



def train_model(X_train, y_train):   
    """
    Treina um modelo de regressão linear usando os dados fornecidos.

    Args:
    - data_path (str): Caminho para os dados processados.

    Returns:
    - model: Modelo treinado.
    """

    # Treinar um modelo simplificado
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def save_model(model, model_path='trained_model.pkl'):
    """
    Salva o modelo treinado em um arquivo.

    Args:
    - model: Modelo treinado.
    - model_path (str): Caminho para salvar o modelo.
    """
    try:
        joblib.dump(model, model_path)
        print(f"Modelo salvo com sucesso em {model_path}")
    except Exception as e:
        print(f"Erro ao salvar o modelo: {e}")

def load_model(model_path='trained_model.pkl'):
    """
    Carrega um modelo treinado de um arquivo.

    Args:
    - model_path (str): Caminho para o arquivo do modelo.

    Returns:
    - model: Modelo carregado.
    """
    try:
        model = joblib.load(model_path)
        print(f"Modelo carregado com sucesso de {model_path}")
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None

def predict(model, data):
    """
    Faz previsões usando o modelo fornecido.

    Args:
    - model: Modelo treinado.
    - data (DataFrame): Dados para previsão.

    Returns:
    - predictions: Previsões do modelo.
    """
    try:
        predictions = model.predict(data)
        return predictions
    except Exception as e:
        print(f"Erro ao fazer previsões: {e}")
        return None

if __name__ == "__main__":
    # Treinando o modelo
    trained_model = train_model()
    save_model(trained_model)
