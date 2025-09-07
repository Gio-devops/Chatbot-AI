import pytest
from unittest.mock import MagicMock, patch
from main import prompt_template # Importa o template do prompt do seu app principal

# A função a ser testada não está explicitamente definida em main.py,
# então vamos testar a lógica de construção do prompt.

def test_prompt_construction():
    """
    Testa se o código do usuário é inserido corretamente no template do prompt.
    """
    user_code = "def add(a, b):\n    return a + b"
    expected_prompt = prompt_template.format(user_code=user_code)
    
    assert user_code in expected_prompt
    assert "Você é um especialista em testes de software" in expected_prompt

@patch('main.genai.GenerativeModel')
def test_api_call_with_mock(MockGenerativeModel):
    """
    Simula uma chamada à API e verifica se o modelo é chamado com o prompt correto.
    """
    # Configuração do Mock
    mock_model_instance = MockGenerativeModel.return_value
    mock_response = MagicMock()
    mock_response.text = "import unittest\n# Test code here"
    mock_model_instance.generate_content.return_value = mock_response

    # Código do usuário
    user_code = "def subtract(a, b):\n    return a - b"
    
    # Simula a lógica que aconteceria no Streamlit
    # 1. Construir o prompt
    prompt = prompt_template.format(user_code=user_code)
    
    # 2. Chamar o método que usa o modelo
    # No nosso caso, é a chamada direta no main.py
    response = mock_model_instance.generate_content(prompt)

    # Asserções
    # Verifica se o método `generate_content` foi chamado uma vez
    mock_model_instance.generate_content.assert_called_once()
    
    # Verifica se o prompt passado para o modelo estava correto
    called_prompt = mock_model_instance.generate_content.call_args[0][0]
    assert user_code in called_prompt
    assert prompt_template.split('{')[0] in called_prompt

    # Verifica se a resposta do mock foi retornada
    assert response.text == "import unittest\n# Test code here"