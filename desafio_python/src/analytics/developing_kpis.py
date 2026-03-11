import collections
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