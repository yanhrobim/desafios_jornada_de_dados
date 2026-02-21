from read_raw_file import read_csv_file
import collections


relatorio_individual = read_csv_file("./data/report/relatorio_individual.csv")

quantidade_funcionario_area = {}
count = collections.Counter()
for dados in relatorio_individual:
    areas = dados

    if dados["area"] == "TI":


        count[dados["area"]] += 1
        quantidade_funcionario_area.update({"TI": count["TI"]})


print(quantidade_funcionario_area)

