from src.analytics.developing_kpis import quantidade_funcionario_por_area, media_salario_por_area, kpi_bonus_geral_total, top3_funcionarios_maior_bonus_final
import json

def create_kpis_json_file(relatorio_individual: list, path_to_kpis_json: str):
    """
    # Function create_kpis_json_file
    Função para a criação do arquivo: **.json** (Arquivo este que possuí métricas agregadas e dados estratégicos)

    Args:
        relatorio_individual (list): Arquivo CSV após a limpeza de dados do pipeline, sendo salvo como padrão em: './data/report/'
        path_to_kpis_json (str): Path para o local desejado onde o arquivo **json** deve ser armazenado.

    ### KPIs disponíveis:

        'Quantidade de Funcionários Por Área'
        'Media de Salário Por Área'
        'Bonus Total Geral'
        'Top 3 Funcionários Com Maior Bonus Final'

    Returns:
            file.json (json): Arquivo JSON que possuí dados com métricas agregadas (KPIs), tornando-os estratégicos para decisões de negócio.
            Sendo recomendando salva-lo em ``'./data/report/'`` visando manter a organização do projeto e desafio.

    """
        
    try:
        quantidade_funcionario_de_por_area = quantidade_funcionario_por_area(relatorio_individual)
        print("KPI: 'Quantidade de Funcionários Por Área' Desenvolvida!\n")    
    except Exception as e:
        print(f"Algum erro aconteceu na criação da KPI: 'Quantidade de Funcionários Por Área'... Error: {e}")
        pass

    try:
        media_salario_de_por_area = media_salario_por_area(relatorio_individual)
        print("KPI: 'Media de Salário Por Área' Desenvolvida!\n")
    except Exception as e:
        print(f"Algum erro aconteceu na criação da KPI: 'Media de Salário Por Área'... Error: {e}")
        pass

    try:
        bonus_geral_total = kpi_bonus_geral_total(relatorio_individual)
        print("KPI: 'Bonus Total Geral' Desenvolvida!\n")
    except Exception as e:
        print(f"Algum erro aconteceu na criação da KPI: 'Bonus Total Geral... Error: {e}")
        pass

    try:
        top3_funcionarios_com_maior_bonus_final = top3_funcionarios_maior_bonus_final(relatorio_individual)
        print("KPI: 'Top 3 Funcionários Com Maior Bonus Final' Desenvolvida!\n") 
    except Exception as e:
        print(f"Algum erro aconteceu na criação da KPI: 'Bonus Total Geral... Error: {e}")
        pass

    # Try/Exccept adicionado logo após o desenvolvimento das KPIs, visando auxiliar melhor a entender o momento em que o código está dando algum erro/exeção.

    try:
        kpis = {}
        kpis.update({'KPI':{'Quantidade de Funcionario Por Área': quantidade_funcionario_de_por_area,
                        'Media de Salario Por Área': media_salario_de_por_area,
                        'Bonus Total Geral': bonus_geral_total,
                        'Top 3 Funcionarios com Maior Bonus Final': top3_funcionarios_com_maior_bonus_final}})
    except Exception as e:
        print(f"Ocorreu um erro na criação do dict! KPIs iriam ser juntadas em um dict sendo posteriormente salvas como json... Error: {e}")
        pass
    else:
        if kpis:
            with open(f"{path_to_kpis_json}", "w", encoding='utf-8') as kpis_json:
                json.dump(kpis, kpis_json, indent=4, sort_keys=True, ensure_ascii=False)

            print(f"Todas as KPIs foram criadas e desenvolvidas corretamente, a partir do arquivo CSV recebido. File .json está finalizado e localizado em: '{path_to_kpis_json}'")