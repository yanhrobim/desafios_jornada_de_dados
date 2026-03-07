import streamlit as st
import pandas as pd
from src.ingestion.read_raw_file import read_csv_file
from src.analytics.developing_kpis import media_salario_por_area, quantidade_funcionario_por_area


st.set_page_config(page_title="Colaboradores", layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.title('👨‍💼Funcionários')
    st.markdown('### *Dados de Colaboradores da Empresa*')

    st.subheader(' Relatório Individual')
    relatorio_individual = read_csv_file("/home/usuario/Projetos/desafios_jornada_de_dados/desafio_python/data/report/relatorio_individual.csv")

    st.table(relatorio_individual)

with col2:

    df = pd.read_json("./data/kpis/kpis.json")

    st.subheader("Média de Salario Por Área")

    KPI_media_salario_por_area = st.bar_chart(df['KPI']['Media de Salario Por Área'], height=275)
    