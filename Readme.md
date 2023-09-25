# Car-Price-Prediction - Previsão de Preço Médio 🚀 🔄 🌐

Codificação em Python para projeto completo em 'Data Science de Car Price Prediction' é uma aplicação de aprendizado de máquina que utiliza técnicas de regressão. Seu objetivo é prever o preço médio de carros com base em diversos atributos. Este projeto não só evidencia a eficácia do aprendizado de máquina, mas também demonstra o potencial da ciência de dados em trazer insights valiosos para setores tradicionais, como o automobilístico.
Nesta versão, a informação foi condensada e as repetições foram eliminadas, tornando a descrição mais direta e clara.


## 📓 Notebooks do Projeto

Durante o desenvolvimento deste projeto, utilizei Notebooks para realizar Análises Exploratórias e Treinamento de Modelos. Estes notebooks são essenciais para entender os dados e iterar rapidamente sobre diferentes modelos e parâmetros.

### EDA.ipynb

**Análise Exploratória de Dados (EDA)**

Neste notebook, realizei uma Análise detalhada dos dados disponíveis. Usando uma variedade de gráficos e técnicas estatísticas, conseguimos entender as distribuições, relações e padrões nos dados. Algumas das visualizações incluem:

- Distribuições de variáveis individuais
- Correlações entre variáveis
- Gráficos de caixa para entender a dispersão e outliers
- Gráficos de tendência ao longo do tempo (se aplicável)

Este notebook é fundamental para qualquer Cientista de Dados entender profundamente os dados à sua disposição.

### Model_Training.ipynb

**Treinamento e Avaliação do Modelo**

Após a fase de EDA, passamos para o treinamento do modelo neste notebook. Aqui, experimentamos diferentes algoritmos, ajustamos hiperparâmetros e avaliamos o desempenho do modelo usando métricas relevantes. O notebook inclui:

- Separação dos dados em conjuntos de treinamento e teste
- Treinamento de diferentes modelos de aprendizado de máquina
- Avaliação do desempenho do modelo usando métricas como RMSE, MAE, etc.
- Visualizações de importância de recursos

### Executando os Notebooks

Para executar os notebooks, você pode usar plataformas como o **Jupyter Notebook** localmente ou o **Google Colab** para uma experiência baseada em nuvem. Ambas as plataformas são excelentes para a execução interativa de código e visualização de dados.



## Visão Geral

O código implementa um pipeline de aprendizado de máquina típico, que inclui:

- **Coleta de Dados**: Coleta dados de fontes específicas.
- **Pré-processamento de Dados**: Limpa e transforma os dados para treinamento.
- **Treinamento do Modelo**: Treina um modelo de aprendizado de máquina.
- **Avaliação do Modelo**: Avalia o desempenho do modelo treinado.
- **Previsão**: Usa o modelo treinado para fazer previsões em novos dados.

##  Como Rodar a Aplicação 🚀

```
pip install -r requirements.txt
```

```
pip install jupyter

```

- Comandos para rodar no Windows
```
venv\Scripts\activate 
```

```
python -m venv venv

```

- Comandos para rodar Linux
```
source venv/bin/activate

```

```
python3 -m venv venv

```


## Como Usar

Para executar o projeto, siga os comandos abaixo:

- Coleta de dados: Esta etapa envolve coletar dados de um ou mais fontes, como um banco de dados, um arquivo CSV ou um site.

Rode o comando para compilar a primeira fase do projeto

```
python main.py --collect_data
```

- Pré-processamento de dados: Esta etapa envolve limpar os dados, removendo outliers e valores ausentes, e transformando os dados em um formato adequado para o treinamento do modelo.

Rode o comando para compilar a segunda fase do projeto
```
python main.py --preprocess´
```

- Treinamento do modelo: Esta etapa envolve treinar um modelo de aprendizado de máquina, como uma regressão linear ou uma regressão com árvores de decisão, usando os dados pré-processados.
Avaliação do modelo: Esta etapa envolve avaliar o desempenho do modelo treinado em um conjunto de dados de teste separado.

Rode o comando para compilar a terceira fase do projeto
```
python main.py --train
```

- Previsão: Esta etapa envolve usar o modelo treinado para fazer previsões em novos dados.
O código que você forneceu também implementa um argumento de linha de comando --predict, que permite que você use o modelo treinado para fazer previsões em novos dados. Isso pode ser útil para aplicativos de produção, como um sistema que prevê o preço de uma casa com base em suas características.

Rode o comando para compilar a quarta fase do projeto
```
python main.py --predict

```

## 📖 Storytelling do Projeto

### Introdução

O mundo dos automóveis é vasto e diversificado. Com tantas variáveis, como marca, modelo, tipo de combustível, tração, entre outras, determinar o preço médio de um carro pode ser um desafio. É aqui que entra a ciência de dados, permitindo-nos usar essas variáveis para prever o preço médio de um carro com base em suas características.

### Objetivo

O principal objetivo deste projeto é desenvolver um modelo de aprendizado de máquina que possa prever o preço médio de um carro com base em suas características. Ao fazer isso, podemos fornecer insights valiosos para concessionárias, compradores e vendedores sobre o valor justo de um carro no mercado.

### Pipeline do Projeto

1. **Coleta de Dados**: Iniciamos coletando dados relevantes sobre carros. Isso pode incluir dados de várias fontes, como bancos de dados, arquivos CSV ou até mesmo scraping de sites.

2. **Pré-processamento de Dados**: Uma vez coletados, os dados passam por um processo de limpeza e transformação. Isso inclui a manipulação de valores ausentes, a conversão de tipos de dados e a codificação de variáveis categóricas.

3. **Treinamento do Modelo**: Com os dados preparados, passamos para a fase de treinamento. Aqui, usamos algoritmos de aprendizado de máquina para treinar um modelo que possa fazer previsões precisas sobre o preço médio de um carro.

4. **Avaliação**: Após o treinamento, avaliamos o desempenho do nosso modelo usando métricas relevantes para garantir que ele seja preciso e confiável.

5. **Previsão**: Com o modelo treinado, agora podemos fazer previsões sobre novos dados. Isso é particularmente útil para avaliar o preço de carros que estão entrando no mercado ou para reavaliar carros com base em novas informações.



### Detalhes
O objetivo deste projeto é prever um valor contínuo, como o preço médio de um produto, com base em outros atributos. 
O argumento --predict permite que você use o modelo treinado para fazer previsões em novos dados, tornando-o útil para aplicativos de produção.



### Conclusão
Este projeto é uma implementação robusta e eficaz de um modelo de regressão. Pode ser adaptado e usado em diversos cenários onde a previsão de valores contínuos é necessária. A estrutura modular do código facilita a expansão e adaptação para diferentes conjuntos de dados e requisitos.


### Autor:
Emerson Amorim
