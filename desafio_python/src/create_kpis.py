from read_raw_file import read_csv_file
import collections
import json


relatorio_individual = read_csv_file("./data/report/relatorio_individual.csv")

def quantidade_funcionario_por_area():
    relatorio_individual = read_csv_file("./data/report/relatorio_individual.csv")

    quantidade_funcionario_area = {}
    count = collections.Counter()
    for dados in relatorio_individual:

        count[dados["area"]] += 1

        quantidade_funcionario_area.update({"Quantidade de Funcionarios na Area de TI": count["TI"],
                                            "Quantidade de Funcionarios na Area de Vendas": count["Vendas"],
                                            "Quantidade de Funcionarios na Area do Financeiro": count["Financeiro"],
                                            "Quantidade de Funcionarios na Area de Operacoes": count["Operações"],
                                            "Quantidade de Funcionarios na Area do RH": count["RH"]})

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
            avg_salario_por_area.update({"Media do Salario na Area de TI": round(media_de_salarios_ti, 2)})
        
        if dados['area'] == 'Vendas':
            salarios_vendas.append(float(dados['salario']))    

            media_de_salarios_vendas = sum(salarios_vendas) / len(salarios_vendas)

            avg_salario_por_area.update({"Media do Salario na Area de Vendas": round(media_de_salarios_vendas, 2)})

        if dados['area'] == 'RH':
                salarios_rh.append(float(dados['salario']))   

                media_de_salarios_rh = sum(salarios_rh) / len(salarios_rh)

                avg_salario_por_area.update({"Media do Salario na Area de RH": round(media_de_salarios_rh, 2)})

        if dados['area'] == 'Operações':
            salarios_operacoes.append(float(dados['salario']))    

            media_de_salarios_operacoes = sum(salarios_operacoes) / len(salarios_operacoes)

            avg_salario_por_area.update({f"Media do Salario na Area de Operacoes": round(media_de_salarios_operacoes, 2)})
            # Para médias que resultam em Dízima Periódica, utilizo o Round para arrendodar o valor real.
            # Com o objetivo de ter/fazer uma validação de dados.

        if dados['area'] == 'Financeiro':
            salarios_financeiro.append(float(dados['salario']))    

            media_de_salarios_financeiro = sum(salarios_financeiro) / len(salarios_financeiro)

            avg_salario_por_area.update({"Media do Salario na Area de Financeiro": round(media_de_salarios_financeiro, 2)})

    return avg_salario_por_area

def bonus_geral_total():
    bonus_de_cada_usuario = []
    bonus_total_geral = {}
    for dados in relatorio_individual:
        bonus_de_cada_usuario.append(float(dados["bonus_final"]))
        bonus_total_geral.update({"Bonus Total Geral": sum(bonus_de_cada_usuario)})

    return bonus_total_geral







