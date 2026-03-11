import streamlit as st

app = st.navigation([st.Page(page="../app/pages/relatorio_individual.py",title="Relatorio Individual", icon='👨‍💼'), 
                     st.Page(page='../app/pages/kpis_dashboard.py', title="Data Visualization", icon='📊')])

st.set_page_config(page_title="Desafio Python")

app.run()