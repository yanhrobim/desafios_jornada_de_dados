import streamlit as st
import pandas as pd
import operator
from src.ingestion.read_raw_file import read_csv_file
from src.analytics.developing_kpis import media_salario_por_area, quantidade_funcionario_por_area


st.set_page_config(page_title="Colaboradores", layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.title('👨‍💼Funcionários')
    st.markdown('### *Dados de Colaboradores da Empresa*')

    st.subheader('Relatório Individual')
    relatorio_individual = read_csv_file("/home/usuario/Projetos/desafios_jornada_de_dados/desafio_python/data/report/relatorio_individual.csv")

    st.table(relatorio_individual)

    df = pd.read_json("./data/kpis/kpis.json")

    st.metric(label="**BONUS TOTAL GERAL 🎁**", value=df['KPI']['Bonus Total Geral']["Bonus Total Geral"])

with col2:


    st.subheader("Média de Salario Por Área")


    KPI_media_salario_por_area = st.bar_chart(data=df['KPI']['Media de Salario Por Área'], height=275)

    st.subheader("Quantidade de Funcionario Por Área")

    KPI_quantidade_funcionario_por_area = st.area_chart(x_label="Área", y_label="Quantidade", data=df['KPI']['Quantidade de Funcionario Por Área'], height=325)

    relatorio_individual_df = pd.DataFrame(relatorio_individual)

    st.subheader("Top Funcionários Com Bonus Final 💵")

    opcao_select = st.select_slider(label="Escolha uma Opção de Ranking", options=['3', '5', '7', '10'])


    relatorio_individual_df['Top'] = relatorio_individual_df['bonus_final'].rank(ascending=False)

    order_by = relatorio_individual_df.sort_values("Top").reset_index(drop=True).head(int(opcao_select))

    st.dataframe(order_by, column_order=['nome', 'area', 'bonus_final', 'Top'], hide_index=True)
