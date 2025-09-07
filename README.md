# Chatbot-AI

# PyUnit Scribe

## Descrição

**PyUnit Scribe** é um agente de IA generativa projetado para automatizar a criação de testes unitários para funções Python. A ferramenta utiliza a API Gemini do Google para analisar o código fornecido e gerar testes completos com a biblioteca `unittest`.

## Objetivo

Acelerar o desenvolvimento de software e melhorar a qualidade do código, reduzindo o tempo e o esforço manual necessários para escrever testes unitários.

## Tecnologias Utilizadas

- Python
- Streamlit (para a interface web)
- Google Gemini (para a geração de código)

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd Chatbot-AI
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure sua API Key:**
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Adicione sua chave da API Gemini ao arquivo da seguinte forma:
      ```
      GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
      ```

4.  **Execute a aplicação:**
    ```bash
    streamlit run main.py
    ```

5.  Acesse a URL fornecida pelo Streamlit em seu navegador.