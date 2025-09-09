# 🤖 Guardian AI: Gerador de Testes Unitários com IA

**Guardian AI** é um agente de IA generativa que automatiza a criação de testes unitários para funções Python. Utilizando o poder da API Gemini do Google, esta ferramenta analisa seu código e gera testes completos com a biblioteca `unittest`, acelerando o ciclo de desenvolvimento e melhorando a qualidade do software.

Este projeto não é apenas uma aplicação de IA, mas um ecossistema completo que incorpora práticas de DevOps, como Infraestrutura como Código (IaC), containerização e um pipeline de CI/CD para simular um ambiente de desenvolvimento profissional.

---

## 📋 Índice

-   [🎯 Sobre o Projeto](#-sobre-o-projeto)
    -   [O Problema](#o-problema)
    -   [A Solução](#a-solução)
    -   [Funcionalidades](#-funcionalidades)
-   [🛠️ Stack Tecnológica](#️-stack-tecnológica)
-   [🚀 Começando: Guia de Instalação e Configuração](#-começando-guia-de-instalação-e-configuração)
    -   [Pré-requisitos](#pré-requisitos)
    -   [Configuração Inicial Passo a Passo](#configuração-inicial-passo-a-passo)
-   [⚙️ Modos de Execução](#️-modos-de-execução)
    -   [1. Execução Local Padrão (para desenvolvimento)](#1-execução-local-padrão-para-desenvolvimento)
    -   [2. Execução com Docker (ambiente padronizado)](#2-execução-com-docker-ambiente-padronizado)
    -   [3. Ambiente de Desenvolvimento Remoto com GitHub Codespaces](#3-ambiente-de-desenvolvimento-remoto-com-github-codespaces)
-   [🏛️ Infraestrutura como Código (IaC) com Terraform](#-infraestrutura-como-código-iac-com-terraform)
-   [🧪 Testes e Qualidade de Código](#-testes-e-qualidade-de-código)
-   [🔄 Pipeline de CI/CD](#-pipeline-de-cicd)
-   [📜 Referência de Comandos (Makefile)](#-referência-de-comandos-makefile)

---

## 🎯 Sobre o Projeto

### O Problema

Escrever testes unitários é uma prática essencial para garantir a robustez e a manutenibilidade do código. No entanto, é uma tarefa repetitiva, demorada e que muitos desenvolvedores adiam, resultando em débito técnico e maior risco de bugs em produção.

### A Solução

**Guardian AI** atua como um engenheiro de QA assistente. Ele automatiza a parte mais trabalhosa da escrita de testes, analisando a lógica, os casos de uso e os possíveis pontos de falha de uma função para gerar um conjunto de testes abrangente. Isso libera o tempo do desenvolvedor para focar na lógica de negócio.

### ✨ Funcionalidades

-   🧠 **Geração Inteligente:** Analisa funções Python e gera testes unitários com `unittest`.
-   🔬 **Cobertura Abrangente:** Cria testes para o caminho feliz, casos extremos (edge cases) e tratamento de exceções.
-   🖥️ **Interface Simples:** Utiliza o Streamlit para uma experiência de usuário intuitiva e direta.
-   📦 **Containerizado:** Empacotado com Docker para garantir consistência entre ambientes.
-   ☁️ **Infraestrutura como Código:** Scripts Terraform para simular o provisionamento da infraestrutura na nuvem.
-   ✅ **Qualidade Garantida:** Pipeline de CI/CD com GitHub Actions para automação de testes e linting.

---

## 🛠️ Stack Tecnológica

| Categoria         | Tecnologia                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| **IA & Backend** | Python 3.10, Google Gemini API (`google-generativeai`)                                                     |
| **Frontend** | Streamlit                                                                                                |
| **DevOps** | Docker, Terraform, GitHub Actions, Makefile                                                              |
| **Testes** | Pytest, Pytest-Mock                                                                                      |
| **Qualidade** | Ruff (Linter)                                                                                            |

---

## 🚀 Começando: Guia de Instalação e Configuração

Siga estes passos para ter o projeto rodando em sua máquina local.

### Pré-requisitos

Certifique-se de que você tem as seguintes ferramentas instaladas:
-   [Git](https://git-scm.com/downloads)
-   [Python 3.10+](https://www.python.org/downloads/)
-   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
-   [Terraform](https://www.terraform.io/downloads) (Opcional, apenas para simulação de IaC)

### Configuração Inicial Passo a Passo

1.  **Clone o Repositório**
    ```bash
    git clone https://github.com/Gio-devops/projeto-final-ia.git
    ```

2.  **Navegue até o Diretório do Projeto**
    ```bash
    cd projeto-final-ia/
    ```

3.  **Obtenha sua Chave de API do Gemini**
    -   Acesse o [Google AI Studio](https://aistudio.google.com/).
    -   Faça login com sua conta Google.
    -   Clique em **"Get API key"** e em **"Create API key in new project"**.
    -   Copie a chave gerada. **Mantenha-a em segurança!**

4.  **Crie e Configure o Arquivo de Variáveis de Ambiente (`.env`)**
    ```bash
    # Linux/macOS
    touch .env

    # Windows (PowerShell)
    New-Item -ItemType File .env
    ```
    Adicione no `.env`:
    ```
    GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
    ```

5.  **Instale as Dependências do Python**
    ```bash
    make install
    ```
    *(Alternativamente: `pip install -r requirements.txt`)*

---

## ⚙️ Modos de Execução

### 1. Execução Local Padrão (para desenvolvimento)

```bash
make run
```

- Inicia o servidor Streamlit local.  
- Acesse [http://localhost:8501](http://localhost:8501) no navegador.

---

### 2. Execução com Docker (ambiente padronizado)

**Passo 1: Construir a Imagem**
```bash
make docker-build
```

**Passo 2: Rodar o Container**
```bash
make docker-run
```
Acesse [http://localhost:8501](http://localhost:8501).

### 3. Ambiente de Desenvolvimento Remoto com GitHub Codespaces

1. Crie um Codespace a partir do repositório.  
2. Configure sua `GEMINI_API_KEY` como segredo no Codespaces.  
3. Execute:
```bash
make run
```
O Codespaces abrirá a porta exposta em uma nova aba.

## 🏛️ Infraestrutura como Código (IaC) com Terraform

```bash
cd terraform
terraform init
terraform plan
```
Simula criação de instância EC2 e grupo de segurança (sem custo real sem credenciais AWS).

## 🧪 Testes e Qualidade de Código

**Rodar testes (pytest):**
```bash
make test
```
**Rodar linter (Ruff):**

```bash
make lint
```

## 🔄 Pipeline de CI/CD

Definido em `.github/workflows/pipeline.yml`.  
Executa automaticamente em **push/pull request** para a branch `main`:

- ✅ Checkout  
- 🐍 Setup Python  
- 📦 Install Dependencies  
- 🔎 Lint (Ruff)  
- 🧪 Testes (pytest)  
- 🐳 Docker Build (simulação)  

## 📜 Referência de Comandos (Makefile)

| Comando            | Descrição                                                            |
| ------------------ | -------------------------------------------------------------------- |
| `make install`     | Instala todas as dependências do `requirements.txt`.                 |
| `make lint`        | Executa o linter Ruff para verificar a qualidade do código.          |
| `make test`        | Executa os testes automatizados com pytest.                          |
| `make run`         | Inicia a aplicação Streamlit localmente.                             |
| `make docker-build`| Constrói a imagem Docker da aplicação com a tag `guardian-ai`.     |
| `make docker-run`  | Inicia um container Docker a partir da imagem, expondo a porta 8501. |
