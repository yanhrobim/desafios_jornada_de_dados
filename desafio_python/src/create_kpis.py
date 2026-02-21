from read_raw_file import read_csv_file
import collections
import json


def quantidade_funcionario_por_area(path_to_kpis_json: str):
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
        
    with open(path_to_kpis_json, 'w', encoding='utf-8') as kpis_json:
        
        json.dump(quantidade_funcionario_area, kpis_json, indent=4)

quantidade_funcionario_por_area(path_to_kpis_json="./data/kpis/kpis.json")

