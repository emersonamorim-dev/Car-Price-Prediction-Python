import argparse
from main import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline para projeto de previsão de preços de carros.")
    parser.add_argument('--all', action='store_true', help="Executa todos os passos da pipeline.")
    parser.add_argument('--collect_data', action='store_true', help="Coleta de dados.")
    parser.add_argument('--preprocess', action='store_true', help="Pré-processamento dos dados.")
    parser.add_argument('--train', action='store_true', help="Treinamento do modelo.")
    parser.add_argument('--predict', action='store_true', help="Realizar previsões com o modelo treinado.")
    
    args = parser.parse_args()
    main(args)
