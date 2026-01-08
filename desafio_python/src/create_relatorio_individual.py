import csv

def load_relatorio_final(clean_data: list):
    with open('./data/report/relatorio_individual.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['id', 'nome', 'area', 'salario', 'bonus_percentual', 'bonus_final']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for dados in clean_data:

            csv_writer.writerow({"id": dados['id'],
                                "nome": dados['nome'],
                                "area": dados['area'],
                                "salario": dados['salario'],
                                "bonus_percentual": dados['bonus_percentual'],
                                "bonus_final": dados['bonus_final']})