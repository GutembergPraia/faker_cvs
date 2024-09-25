<h2>Gerador de Massa de Dados Falsos</h2>

Este projeto cria uma massa de dados falsa no formato CSV com as seguintes colunas: NOME, CPF, MATRICULA, EMAIL, CODIGO DO SETOR, CODIGO DO CARGO, DATA DE ADMISSAO, GESTOR. Este arquivo pode ser usado para testes de importação de dados.

<h2>Passos para Configuração</h2>

1. Crie uma máquina virtual:
    ```bash
    python -m venv .venv
    ```   

2. Habilite a execução de script no terminal:
    ```bash
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    ```

3. Entre na máquina virtual criada:
    ```bash
    .venv\Scripts\activate
    ```

4. Instale a biblioteca faker:
    ```python
    pip install faker
    ```

5. Instale a biblioteca pandas:
    ```python
    pip install pandas
    ```

6. executar
    ```bash
    python.exe gerar_massa_de_dados.py
    ```

