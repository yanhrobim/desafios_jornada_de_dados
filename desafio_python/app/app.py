# Módulo para inciar o Streamlit App.

import streamlit as st

def run_app():
    app = st.navigation([st.Page(page="../app/pages/relatorio_individual.py",title="Relatorio Individual", icon='👨‍💼'), 
                     st.Page(page='../app/pages/kpis_dashboard.py', title="Data Visualization", icon='📊')])

    st.set_page_config(page_title="Desafio Python")

    app.run()

if __name__ == '__main__':
    run_app()