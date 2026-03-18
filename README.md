# Desafios Disponibilizados Jornada de Dados

* [🖊️ Jornada de Dados](#️-sobre-a-jornada)
* [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [🤔 O Por que Deste Repositório](#-o-por-que-deste-repositório)
* [🐍 Desafio Python](#-desafio-python)
  * [📖 Contexto](#-contexto)
  * [📌 Objetivos do Desafio](#-objetivos-do-desafio)
  * [📊 Dashboards (Bônus)](#-dashboards)
* [🛢️ Desafio SQL](#-desafio-sql)

---

## 🖊️ Sobre a Jornada

A ([Jornada de Dados](https://suajornadadedados.com.br/)) é um roadmap voltado para estudos da área de dados em programação como: *Engenharia de Dados*, *Ciência de Dados* e *Análise de Dados*. O roadmap contém **bootcamps** e workshops para aprendizagem de ferramentas e linguagens amplamente utilizadas na área, através de práticas, projetos e exercícios, visando auxiliar no desenvolvimento das habilidades dentro daquilo que se deseja aprender.

## 🚀 Tecnologias Utilizadas

* Python  
* Pandas *(somente para fins de dashboard)*  
* Streamlit  
* SQL *(em desenvolvimento)*  

## 🤔 O Por que Deste Repositório

Com o objetivo de retomar e reforçar os estudos de programação voltados à área de dados, utilizei desafios disponibilizados pelo roadmap Jornada de Dados para prática de **Python** e **SQL**, visando melhorar a lógica de programação nessas linguagens.

Em resumo, um repositório voltado para prática e evolução das habilidades.

## 🧪 Desafio Python

Antes de qualquer coisa, tive a escolha de fazer o desafio em Python puro, não a fim de **"reinventar a roda"**, mas sim para entender melhor a linguagem, explorar módulos nativos e principalmente melhorar a lógica de programação.

### 📖 Contexto

Simulando um cenário real, foi recebido o arquivo `funcionarios.csv`, com dados dos colaboradores (funcionários) da empresa, como:

* Nome  
* Área em que trabalha  
* Salário  

* Para visualizar a documentação completa do desafio (introdução, objetivos e regras de validação), consulte o [README](../desafios_jornada_de_dados/desafio_python/README.md), localizado em `./desafio_python/`.

* Dentro dos módulos `.py` presentes no repositório, onde estão as soluções, existem algumas observações em comentários (`#`), com o objetivo de documentar o raciocínio utilizado e o porquê das escolhas feitas na implementação.

### 📌 Objetivos do Desafio 

1. ***Validação de Dados em Cada Registro***:  
Limpeza dos dados no arquivo `funcionarios.csv`, com o objetivo de obter dados válidos para a geração do arquivo `relatorio_individual.csv`, que posteriormente será utilizado como base para a criação do `kpis.json`.

2. ***Calcular Bônus Final de Cada Colaborador***:  
Calcular o bônus final de cada funcionário com base na fórmula:

```
bonus_final = BONUS_BASE (1000) + salario * bonus_percentual
```

3. ***Gerar Relatórios***:

* `relatorio_individual.csv`: contém apenas registros válidos seguindo as regras de negócio e com o cálculo correto de **bonus_final**.  

* `kpis.json`: métricas agregadas com foco em geração de dados estratégicos. KPIs:

  * quantidade de funcionários por área  
  * média de salário por área  
  * bônus total geral  
  * top 3 funcionários com maior bônus final  

---

### 📊 Dashboards (Bônus)

Apesar de ser um volume extremamente baixo de dados, tive a iniciativa de praticar meus estudos com **Streamlit**, utilizando os dados finais do exercício (como as KPIs solicitadas), com foco em criar um dashboard para visualização dos dados de forma clara.

Também é possível utilizar o `relatorio_individual.csv` para visualizar os dados limpos de cada colaborador.

---

**Demo**:  
https://desafio-python-dashboard.streamlit.app/kpis_dashboard

### 📈 Relatório Individual

![Relatório Individual](/desafio_python/app/images/relatorio_individual_dash.png)

### 📊 KPIs

![KPIs](/desafio_python/app/images/kpis_dash.gif)

## 🛢️ Desafio SQL

<<<<<<< HEAD
In processo... ⌛
=======
In process... ⌛
>>>>>>> ea4893427eefe5c3c102e2afac9170b16a81f691
