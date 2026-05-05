# 🧮 Calculation Toolkit

Aplicação CLI (Command Line Interface) desenvolvida em Python para realizar cálculos básicos de forma interativa.

Este projeto foi criado com o objetivo de praticar conceitos fundamentais de programação, organização de código e boas práticas utilizadas no mercado.

---

## 🚀 Funcionalidades

* 🌡️ Conversão de temperatura (Celsius → Fahrenheit)
* 🔢 Cálculo de fatorial
* 📥 Entrada de dados com validação
* 🧠 Tratamento de erros (entrada inválida)
* 🧩 Código modularizado (separação por responsabilidades)

---

## 📁 Estrutura do projeto

```
calculation-toolkit/
│
├── main.py
├── services/
│   ├── temperatura.py
│   └── fatorial.py
│
├── utils/
│   └── input_helper.py
│
├── README.md
└── .gitignore
```

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca padrão `math`

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/calculation-toolkit.git
```

### 2. Acesse a pasta do projeto

```bash
cd calculation-toolkit
```

### 3. Execute a aplicação

```bash
python main.py
```

---

## 💻 Exemplo de uso

```
=== Calculation Toolkit ===
1 - Converter Celsius para Fahrenheit
2 - Calcular Fatorial
0 - Sair

Escolha uma opção: 1
Digite a temperatura em Celsius: 25
Resultado: 77.00 °F
```

---

## 📚 Conceitos aplicados

* Entrada de dados com `input()`
* Conversão de tipos (`int`, `float`)
* Estrutura condicional (`if/elif`)
* Tratamento de exceções (`try/except`)
* Modularização de código
* Boas práticas (PEP 8)

---

## 📈 Melhorias futuras

* Interface gráfica (Tkinter)
* Versão web com Flask
* Testes automatizados
* Empacotamento como executável

---

## 👨‍💻 Autor

Desenvolvido por Rodrigo Mayer Alves
