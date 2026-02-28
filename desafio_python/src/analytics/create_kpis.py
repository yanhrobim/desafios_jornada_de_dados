import collections
import json
import operator

def quantidade_funcionario_por_area(relatorio_individual: list):


    quantidade_funcionario_area = {}

    count = collections.Counter() # Counter() é uma subclasse dict disponível no módulo collections, desenvolvida com o objetivo de contar objetos iteráveis.
                                  # Essa contagem resulta nos elementos sendo armazenados como chave e suas frequências em um Dict.

    for dados in relatorio_individual:

        count[dados["area"]] += 1   # A cada vez que valor de Área(TI, Vendas, Financeiro, Operações, RH)
                                    # for visto no objeto iterável passado, ele aumenta +1. Ex: TI visto e contado 2 vezes, +1 +1 = 2. {"TI": 2} 

        quantidade_funcionario_area.update({"TI": count["TI"],
                                            "Vendas": count["Vendas"],
                                            "Financeiro": count["Financeiro"],
                                            "Operações": count["Operações"],
                                            "RH": count["RH"]})

    return quantidade_funcionario_area

def media_salario_por_area(relatorio_individual):

    avg_salario_por_area = {}

    salarios_ti = []        # Listas criadas para cada área que temos nos nossos dados CSV.
                            # Tendo em vista que, assim podemos armazenar dados de uma área específica na lista que se assemelha.
    salarios_vendas = []
    salarios_rh = []
    salarios_operacoes = []
    salarios_financeiro = []

    for dados in relatorio_individual:

        if dados['area'] == 'TI':
            salarios_ti.append(float(dados['salario']))   # Precisamos de uma lista pois a função sum()  somente faz a soma de objetos iteráveis, tuplas ou conjuntos. 
                                                    # Como estamos em um loop de um Dict, os valores não eram passados de forma sequencial,
                                                    # e sim somente o último valor encontrado da coluna específica.
                                                    # Com umaa lista, o loop For adiciona todos os valores encontrados com append,
                                                    # conseguindo executar a função de soma com todos os valores armazenados da coluna, e não somente o último. 

            media_de_salarios_ti = sum(salarios_ti) / len(salarios_ti)
            avg_salario_por_area.update({"TI": round(media_de_salarios_ti, 2)})
        
        if dados['area'] == 'Vendas':   # If com o objetivo de filtrar dados do dict. Tendo como objetivo pegar somente linhas da área especificada no If, e fazer cálculos e operações somente nas linhas corretas gerando dados mais confiáveis.
            salarios_vendas.append(float(dados['salario']))    

            media_de_salarios_vendas = sum(salarios_vendas) / len(salarios_vendas)

            avg_salario_por_area.update({"Vendas": round(media_de_salarios_vendas, 2)})

        if dados['area'] == 'RH':
                salarios_rh.append(float(dados['salario']))   

                media_de_salarios_rh = sum(salarios_rh) / len(salarios_rh)

                avg_salario_por_area.update({"RH": round(media_de_salarios_rh, 2)})

        if dados['area'] == 'Operações':
            salarios_operacoes.append(float(dados['salario']))    

            media_de_salarios_operacoes = sum(salarios_operacoes) / len(salarios_operacoes)

            avg_salario_por_area.update({f"Operacoes": round(media_de_salarios_operacoes, 2)})
            # Para médias que resultam em Dízima Periódica, utilizo o Round para arrendodar o valor real.
            # Com o objetivo de ter/fazer uma validação de dados, provocando dados mais certeiros e confiavéis.

        if dados['area'] == 'Financeiro':
            salarios_financeiro.append(float(dados['salario']))    

            media_de_salarios_financeiro = sum(salarios_financeiro) / len(salarios_financeiro)

            avg_salario_por_area.update({"Financeiro": round(media_de_salarios_financeiro, 2)})

    return avg_salario_por_area

def kpi_bonus_geral_total(relatorio_individual: list):

    bonus_de_todos = []             # Criando uma váriavel de lista visando que para obtermos dados com cálculo,
                                    # precisamos de todos os dados necessários e de forma iterável (sequencial).
                                    # Mesmo que, executarmos uma função de operação matemática em nossos dados, resultados do loop For,
                                    # nos resulta somente no último valor... Com append, mudamos isso adicionando a uma lista todos os valores que temos. 
    bonus_total_geral = {}

    for dados in relatorio_individual:
        bonus_de_todos.append(float(dados["bonus_final"]))

        bonus_de_cada_usuario = sum(bonus_de_todos)

        bonus_total_geral.update({"Bonus Total Geral": round(bonus_de_cada_usuario, 2)})

    return bonus_total_geral

def top3_funcionarios_maior_bonus_final(relatorio_individual: list):


    top3_funcionarios_list = []

    dados = []

    for linha in relatorio_individual:

        dados.append(linha)

        dados.sort(key=operator.itemgetter('bonus_final'), reverse=True) 
        # Ordenando com sort() todos os valores de bonus_final(float) de forma decrescente com 'reverse=True'.
        # Utilizo o itemgetter(), uma função disponibilizada pelo módulo Operator do Python, para somente fazer a ordenação seguindo valores da coluna (bonus_final), presente na nossa lista de dicionários, sendo nossos dados.

        top = 0

    for top3 in dados[:3]:  # Individualizando cada dicionário(linha de dados) logo após a ordenação.
            top += 1
            top3_funcionarios_list.append({"Nome": str(top3['nome']),
                                    "Bonus_Final": float(top3['bonus_final']),
                                    "Top": int(top)})

    return top3_funcionarios_list

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