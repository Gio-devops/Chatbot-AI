# 1. Usar uma imagem base oficial do Python
FROM python:3.10-slim

# 2. Definir o diretório de trabalho dentro do container
WORKDIR /app

# 3. Definir variáveis de ambiente para o Streamlit e Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV STREAMLIT_SERVER_PORT 8501
ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0

# 4. Copiar e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar o restante do código da aplicação
COPY . .

# 6. Expor a porta que o Streamlit irá usar
EXPOSE 8501

# 7. Comando para iniciar a aplicação quando o container for executado
CMD ["streamlit", "run", "main.py"]