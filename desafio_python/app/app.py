import streamlit as st
import pandas as pd
import operator
from src.ingestion.read_raw_file import read_csv_file
from src.analytics.developing_kpis import media_salario_por_area, quantidade_funcionario_por_area


st.set_page_config(page_title="KPIs Dashboards", layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.title('👨‍💼Funcionários')
    st.markdown('## **Dados de Colaboradores da Empresa**')

    st.subheader('Relatório Individual')
    relatorio_individual = pd.read_csv("/home/usuario/Projetos/desafios_jornada_de_dados/desafio_python/data/report/relatorio_individual.csv")


    st.dataframe(data=relatorio_individual, hide_index=True, height='content')

    df = pd.read_json("./data/kpis/kpis.json")

    KPI_bonus_total_geral = df['KPI']['Bonus Total Geral']["Bonus Total Geral"]

    st.metric(label="**BONUS TOTAL GERAL 🎁**", value=f'R$ {KPI_bonus_total_geral}')

with col2:


    st.subheader("📊 Média de Salario Por Área")

    label_media_salario = st.markdown(r"###### $$\text{Média de Salário Por Área} = \frac{\text{Soma dos Salários (De cada Área Individualmente)}}{\text{Quantidade de Salários (De cada Área Individualmente)}}$$")

    KPI_media_salario_por_area = st.bar_chart(data=df['KPI']['Media de Salario Por Área'], height=275)


    st.subheader("Quantidade de Funcionarios Por Área 👔")

    KPI_quantidade_funcionario_por_area = st.area_chart(x_label="Área", y_label="Quantidade", data=df['KPI']['Quantidade de Funcionario Por Área'], height=325)


    st.subheader("Top Funcionários Com Bonus Final 🤑")

    opcao_select = st.select_slider(label="Escolha uma Opção de Ranking", options=['3', '5', '7', '10'])


    relatorio_individual['Top'] = relatorio_individual['bonus_final'].rank(ascending=False, method='min') 
    # Criando uma coluna no Dataframe (Top). Tal coluna armazena uma classificação em Ranking baseada nos valores da coluna 'bonus_final' organizando-os de forma decrescente segundo os dados.
    # Para a criação da coluna Top, utilizei o método rank() para ordenar e classificar em forma de Top1, Top2, seguindo os valores da coluna 'bonus_final'. Rank() é principalmente útilizado para atribuir posíção a cada elemento de uma Series ou coluna de um Dataframe em forma de Ranking.
    # 'ascending=False' Paramêtro adicionado ao método com o objetivo de o mesmo entregar os maiores valores primeiro, resumidamente de forma decrescente. 'method='min'' paramêtro  'min' método de desempate simula um estilo competição. (Tendo em vista que valores iguais, ambos recebem o mesmo Rank.)

    order_by = relatorio_individual.sort_values("Top").reset_index(drop=True).head(int(opcao_select)) 
    # sort_values() resulta em uma ordenação/organização de valores. 
    # Utilização do método reset_index() para excluir o antigo index com 'drop=True' e criar um novo seguindo os novos critérios dos dados. 
    # Método head() para executar um limite de linhas selecionadas no Dataframe, seguindo o valor que for escolhido em 'opcao_select' (Select Slider do Streamlit).
    # rank() e sort_values() nesse contexto são muito semelhantes podendo até gerar a conclusão que somente sort_values() seria necessário no código. Mas, optei por adicionar rank() na lógica para a criação da coluna 'Top' e métodos de empate como 'min' escolhido para a lógica do código.

    st.dataframe(order_by, column_order=['nome', 'area', 'bonus_final', 'Top'], hide_index=True)
