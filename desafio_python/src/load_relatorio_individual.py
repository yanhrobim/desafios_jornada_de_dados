import re
from read_raw_file import read_csv_file
from clean_data import clean_data
from read_raw_file import read_csv_file
import csv
import os

funcionários_csv = './data/raw/funcionarios.csv'
read_file = read_csv_file(funcionários_csv)
clean = clean_data(read_file)

with open('./data/report/relatorio_individual.csv', 'a', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'nome', 'area', 'salario', 'bonus_percentual', 'salario_com_bonus']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for dados in clean:

        csv_writer.writerow({"id": dados['id'],
                             "nome": dados['nome'],
                             "area": dados['area'],
                             "salario": dados['salario'],
                             "bonus_percentual": dados['bonus_percentual'],
                             "salario_com_bonus": dados['salario_com_bonus']})
