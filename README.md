# Análise de Teste A/B para Otimização de Página de E-commerce utilizando dados sintéticos

![Status](https://img.shields.io/badge/status-concluído-brightgreen)

## 📝 Descrição do Projeto

Este projeto consiste na análise completa de um teste A/B para um site de e-commerce. O objetivo foi avaliar se um novo design de página de produto (Layout B) resultava em uma taxa de adição ao carrinho superior em comparação com o design antigo (Layout A). A análise foi conduzida utilizando dados sintéticos gerados com a biblioteca Faker para aprendizado e abrange desde a estruturação do teste, análise estatística com Teste Qui-Quadrado, até a formulação de recomendações de negócio.

---

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para manipulação e análise de dados.
* **Faker:** Para geração de dados sintéticos.
* **Matplotlib & Seaborn:** Para visualização de dados.
* **SciPy:** Para a execução do teste estatístico (Qui-Quadrado).
* **Jupyter Notebook:** Como ambiente de análise.
* **Git & GitHub:** Para controle de versão e publicação.

---

## 📈 Resultados-Chave

A análise estatística revelou um **p-valor de 0.0000**, indicando uma diferença estatisticamente significativa entre os dois grupos.

![Gráfico de Conversão](https://i.imgur.com/OiFM2t4.png)  **Conclusão:** O Layout B demonstrou ser significativamente mais eficaz, aumentando a taxa de adição ao carrinho.

**Recomendação Principal:** Implementar o Layout B como padrão para 100% do tráfego do site para maximizar a conversão.

---

## 📂 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/renanrbf/analise_dados_marketing_faker
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Crie o ambiente
    python -m venv venv

    # Ative o ambiente (Windows)
    .\venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Primeiro, gere o arquivo `requirements.txt` com o comando `pip freeze > requirements.txt` no seu terminal com o venv ativo)*

4.  **Execute o Jupyter Notebook:**
    Abra o arquivo `notebooks/analise_teste_ab.ipynb` em um ambiente como Jupyter Lab ou VS Code.

---

## 👨‍💻 Autor

**Renan Ballerini Farinácio**

* **LinkedIn:** https://www.linkedin.com/in/renanfarinacio/
* **GitHub:** https://github.com/renanrbf