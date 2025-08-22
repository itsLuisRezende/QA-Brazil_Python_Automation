# QA-Brazil Python Automation

## 1. Objetivo do projeto
Criar uma suíte de testes automatizados em Python, organizada de forma modular, seguindo boas práticas de nomenclatura e legibilidade. O projeto visa aplicar padrões de automação de testes, com foco em clareza de código e reutilização de componentes.

## 2. Resultado
O resultado foi um framework de testes com arquivos bem estruturados (`data.py`, `helpers.py`, `pages.py`, `main.py`, `test.py`) e convenções definidas (como `snake_case` para variáveis, testes prefixados com `test_`, etc.). Essa base sustenta a criação de testes claros, eficientes e fáceis de manter, com boa separação de responsabilidades.

## 3. Ferramentas utilizadas
- **Python** – linguagem principal para implementação dos testes  
- **Modularidade no código** – uso de arquivos como `helpers`, `pages` e `data` para organização logicamente separada  
- **requirements.txt** – para controle de dependências do projeto

## 4. O que eu aprendi (habilidades/competências adquiridas)
- Aplicação de convenções de código como `snake_case` para variáveis e nomenclatura clara de testes com `test_`  
- Organização modular usando arquivos específicos para dados, páginas, utilidades e execução  
- Importância de evitar esperas desnecessárias para otimizar a execução dos testes  
- Documentar diretrizes no README (como nomenclatura e estrutura) para manter consistência no time

## 5. Existem melhorias a serem feitas?
- Integrar **frameworks de test automation** como `pytest` para execução estruturada dos testes  
- Adicionar **ferramentas de automação de UI** (Selenium, Playwright) para testes de interface web  
- Implementar **integração contínua (CI)** com GitHub Actions para execução automática em cada push  
- Criar **relatórios estruturados** (por exemplo, com Allure) para visualizar o status dos testes

# Diretrizes de nomenclatura de código

- **Nomes de variáveis** são escritos em `snake_case` e descrevem sua finalidade;
- **Constantes** são escritas em maiúsculas;
- **Comentários** são usados para explicar blocos importantes de código;
- A **organização do código** é modular, com blocos de código reutilizáveis importados para onde for necessário;
- Evite funções de espera (`wait`) desnecessárias que fazem com que o teste seja executado por mais tempo do que o necessário;
- Siga uma **convenção de nomenclatura** para títulos de teste que começam com `test\_` e fornece uma descrição clara do cenário de teste. Os títulos dos testes são fornecidos no resumo.
