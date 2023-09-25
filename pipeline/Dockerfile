FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o container
COPY . .

# Exponha a porta que sua API usará
EXPOSE 8500

# Comando para iniciar sua aplicação
CMD ["python", "main.py"]
