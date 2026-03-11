import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title("KPIs Dashboards 📊")

kpis_json = pd.read_json("./data/kpis/kpis.json")
relatorio_individual = pd.read_csv("./data/report/relatorio_individual.csv")

bonus_total_geral = kpis_json['KPI']['Bonus Total Geral']['Bonus Total Geral']

coluna1, meio, coluna2 = st.columns(3) # Criação de Colunas apenas para colocar "Bonus Total Geral" no meio do App Web.

with meio:
    st.subheader("Bonus Total Geral")

    st.subheader(f"RS $ {bonus_total_geral}")

st.markdown('---')

col1, col2, col3 = st.columns(3)

with col1:
    
    st.subheader("Média de Salario Por Área")

    KPI_media_salario_por_area = st.bar_chart(x_label="Salário", y_label="Área", data=kpis_json['KPI']['Media de Salario Por Área'])

with col2:


    st.subheader("Quantidade de Funcionários Por Área ")

    KPI_quantidade_funcionario_por_area = st.bar_chart(x_label="Área", y_label="Quantidade", data=kpis_json['KPI']['Quantidade de Funcionario Por Área'], horizontal=True, height=315)


with col3:

    st.subheader("Top Funcionários Com Bonus Final")

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
