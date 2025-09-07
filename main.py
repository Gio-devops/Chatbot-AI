import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a API Key do Gemini
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    st.error(f"Erro ao configurar a API do Gemini. Verifique sua API_KEY: {e}")
    st.stop()

# --- Configuração do Modelo Generativo ---
# Define as configurações de geração de conteúdo
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# Define as configurações de segurança
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Inicializa o modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# --- PROMPT para o Agente de IA ---
# Este prompt instrui o modelo sobre como ele deve se comportar
prompt_template = """
Você é um especialista em testes de software e engenharia de qualidade (QA) para a linguagem Python.
Seu objetivo é criar testes unitários completos e eficazes para funções Python, utilizando a biblioteca `unittest`.

**Instruções:**
1.  Analise a função Python fornecida pelo usuário.
2.  Identifique os principais cenários a serem testados:
    * **Caminho Feliz:** Teste com entradas válidas e esperadas.
    * **Casos Extremos (Edge Cases):** Teste com valores limites, como 0, -1, listas vazias, strings vazias, etc.
    * **Casos de Erro:** Teste como a função se comporta com entradas inválidas (ex: tipos de dados incorretos), esperando que exceções como `TypeError` ou `ValueError` sejam levantadas.
3.  Gere um código Python completo que importe a biblioteca `unittest` e a função a ser testada (assuma que a função está em um arquivo chamado `main.py`).
4.  Crie uma classe de teste que herde de `unittest.TestCase`.
5.  Dentro da classe, crie métodos de teste claros e descritivos para cada cenário identificado. Use os métodos de asserção do `unittest` (ex: `assertEqual`, `assertTrue`, `assertRaises`).
6.  Inclua o boilerplate `if __name__ == '__main__': unittest.main()` para que o script seja executável.
7.  Retorne **APENAS** o código do teste, sem explicações adicionais, a menos que seja solicitado.

**Função a ser testada:**
```python
{user_code}
```

**Código do Teste Unitário:**
"""

# --- Interface do Streamlit ---
st.set_page_config(page_title="PyUnit Scribe - Chatbot com Google Gemini", page_icon="🤖")
st.title("🤖 PyUnit Scribe")
st.write("Seu assistente de IA para a geração automática de testes unitários em Python.")
st.write("Cole sua função Python abaixo e obtenha o código de teste com unittest instantaneamente.")

# Área de texto para o usuário inserir o código
user_code = st.text_area("Cole sua função Python aqui:", height=200, placeholder="def somar(a, b):\n    return a + b")

if st.button("Gerar Testes Unitários"):
    if user_code:
        with st.spinner("Analisando sua função e gerando testes..."):
            try:
                # Formata o prompt com o código do usuário
                prompt = prompt_template.format(user_code=user_code)

                # Chama a API do Gemini para gerar o conteúdo
                response = model.generate_content(prompt)

                # Exibe o resultado
                st.subheader("✅ Testes Gerados com Sucesso!")
                st.code(response.text, language='python')

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar os testes: {e}")
    else:
        st.warning("Por favor, insira o código de uma função Python para gerar os testes.")

st.sidebar.header("Sobre o Projeto")
st.sidebar.info(
    "Este é um projeto da disciplina de IA Generativa, projetado para resolver um "
    "problema prático de engenharia de software usando a API Gemini do Google."
)
st.sidebar.markdown("---")
st.sidebar.header("Exemplo de Função para Testar")
st.sidebar.code("""
def calcular_fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("A entrada deve ser um inteiro não negativo")
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)
""", language='python')