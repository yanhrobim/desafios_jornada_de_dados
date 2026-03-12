import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('👨‍💼Colaboradores')

st.markdown('##### Dados de Funcionários da Empresa')

st.markdown("---")

st.subheader('Relatório Individual')

relatorio_individual = pd.read_csv("./desafio_python/data/report/relatorio_individual.csv")

st.dataframe(data=relatorio_individual, hide_index=True)