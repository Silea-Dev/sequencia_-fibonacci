# Fibonacci Generator: Abordagem Orientada a Objetos (POO)

![Badge Python](https://img.shields.io/badge/python-3.x-blue) ![Badge POO](https://img.shields.io/badge/paradigma-POO-orange) ![Badge Clean Code](https://img.shields.io/badge/code-clean-green)

## 🚀 Visão Geral

Este projeto é uma implementação do algoritmo clássico da **Sequência de Fibonacci**, estruturado para demonstrar princípios de **Engenharia de Software**, especificamente **Programação Orientada a Objetos (POO)** e **Clean Code**.

Diferente de scripts simples ou abordagens puramente recursivas (que sofrem com performance), este projeto encapsula a lógica de geração em classes com responsabilidades definidas, garantindo um código legível, testável e escalável.

## ⚙️ Destaques de Arquitetura

O projeto foi refatorado para fugir do paradigma procedural básico.

* **Encapsulamento:** A lógica matemática não está solta no código. Ela pertence a uma classe `Fibonacci` (ou similar), protegendo o estado interno da aplicação.
* **Separação de Responsabilidades:** A camada que *calcula* a sequência é separada da camada que *exibe* os dados ao usuário.
* **Performance:** Utilização de abordagem iterativa $O(n)$ para evitar o estouro de pilha (Stack Overflow) comum em implementações recursivas ingênuas $O(2^n)$.

## 🛠️ Tecnologias e Conceitos

* **Linguagem:** Python 3.x
* **Paradigma:** Programação Orientada a Objetos (Classes, Métodos, Atributos).
* **Boas Práticas:** Type Hinting (Tipagem gradual), Docstrings e nomes de variáveis semânticos.

## 💻 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Silea-Dev/sequencia_-fibonacci.git](https://github.com/Silea-Dev/sequencia_-fibonacci.git)
    ```

2.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```

## 🛣️ Roadmap de Estudos

Este projeto serviu como base para consolidar os seguintes conceitos:
- [x] Migração de Lógica Procedural para POO.
- [x] Uso de Type Hints em Python.
- [ ] Implementar a versão "Iterator" (protocolo `__iter__` e `__next__`) para geração sob demanda (Lazy Evaluation).

## Licença

Este projeto está licenciado sob a Licença MIT.
