import streamlit as st
from src.ingestion.read_raw_file import read_csv_file


st.set_page_config(page_title="Colaboradores", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.title('👨‍💼Funcionários')
    st.markdown('*Dados de Colaboradores da Empresa*')

    st.subheader('**Relatório Individual**')
    relatorio_individual = read_csv_file("/home/usuario/Projetos/desafios_jornada_de_dados/desafio_python/data/report/relatorio_individual.csv")

    st.dataframe(relatorio_individual)