.PHONY: help install lint test run docker-build docker-run

help:
	@echo "Comandos disponíveis:"
	@echo "  install       - Instala as dependências do projeto"
	@echo "  lint          - Executa o linter (Ruff) para verificar a qualidade do código"
	@echo "  test          - Executa os testes automatizados com Pytest"
	@echo "  run           - Inicia a aplicação Streamlit localmente"
	@echo "  docker-build  - Constrói a imagem Docker da aplicação"
	@echo "  docker-run    - Executa a aplicação dentro de um container Docker"

install:
	pip install -r requirements.txt

lint:
	ruff check .

test:
	pytest

run:
	python3 -m streamlit run main.py

docker-build:
	docker build -t guardian-ai .

docker-run:
	docker run -p 8501:8501 -e GEMINI_API_KEY=$(shell grep GEMINI_API_KEY .env | cut -d '=' -f2) pyunit-scribe
