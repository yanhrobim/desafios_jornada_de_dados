from read_raw_file import read_csv_file
import collections
import json
import operator


relatorio_individual = read_csv_file("./data/report/relatorio_individual.csv")

def quantidade_funcionario_por_area():
    relatorio_individual = read_csv_file("./data/report/relatorio_individual.csv")

    quantidade_funcionario_area = {}
    count = collections.Counter()
    for dados in relatorio_individual:

        count[dados["area"]] += 1

        quantidade_funcionario_area.update({"TI": count["TI"],
                                            "Vendas": count["Vendas"],
                                            "Financeiro": count["Financeiro"],
                                            "Operações": count["Operações"],
                                            "RH": count["RH"]})

    return quantidade_funcionario_area

def media_salario_por_area():

    relatorio_individual = read_csv_file("./data/report/relatorio_individual.csv")

    avg_salario_por_area = {}
    salarios_ti = []
    salarios_vendas = []
    salarios_rh = []
    salarios_operacoes = []
    salarios_financeiro = []

    for dados in relatorio_individual:

        if dados['area'] == 'TI':
            salarios_ti.append(float(dados['salario']))   # Precisamos de uma lista pois a função sum somente faz a soma de objetos iteráveis, 
                                                    # como estamos em um loop de um Dict, os valores não eram passados de forma sequencial,
                                                    # e sim somente o último valor encontrado da coluna específica.
                                                    # Com a lista, o loop For adiciona todos os valores obtidos com append.

            media_de_salarios_ti = sum(salarios_ti) / len(salarios_ti)
            avg_salario_por_area.update({"TI": round(media_de_salarios_ti, 2)})
        
        if dados['area'] == 'Vendas':
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
            # Com o objetivo de ter/fazer uma validação de dados.

        if dados['area'] == 'Financeiro':
            salarios_financeiro.append(float(dados['salario']))    

            media_de_salarios_financeiro = sum(salarios_financeiro) / len(salarios_financeiro)

            avg_salario_por_area.update({"Financeiro": round(media_de_salarios_financeiro, 2)})

    return avg_salario_por_area

def bonus_geral_total():
    bonus_de_cada_usuario = []
    bonus_total_geral = {}
    for dados in relatorio_individual:
        bonus_de_cada_usuario.append(float(dados["bonus_final"]))
        bonus_total_geral.update({"Bonus Total Geral": sum(bonus_de_cada_usuario)})

    return bonus_total_geral

def top3_funcionarios_maior_bonus_final():
    top3_funcionarios_list = []
    dados = []

    for linha in relatorio_individual:

        dados.append(linha)
        dados.sort(key=operator.itemgetter('bonus_final'), reverse=True)
        top = 0

    for top3 in dados[:3]:
            top += 1
            top3_funcionarios_list.append({"Nome": top3['nome'],
                                    "Bonus_Final": top3['bonus_final'],
                                    "Top": top})

    return top3_funcionarios_list

def create_kpis_json():
    quantidade_funcionario_de_por_area = quantidade_funcionario_por_area()
    media_salario_de_por_area = media_salario_por_area()
    top3_funcionarios_com_maior_bonus_final = top3_funcionarios_maior_bonus_final()

    kpis = {}
    kpis.update({'Quantidade de Funcionario Por Área': quantidade_funcionario_de_por_area, 
                'Media de Salario Por Área': media_salario_de_por_area,
                'Top 3 Funcionarios com Maior Bonus Final': top3_funcionarios_com_maior_bonus_final})


    with open("./data/kpis/kpis.json", "w", encoding='utf-8') as kpis_json:
        json.dump(kpis, kpis_json, indent=4, sort_keys=True, ensure_ascii=False)