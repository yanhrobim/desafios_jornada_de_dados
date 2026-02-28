import csv

def load_relatorio_final(clean_data: list, name_file: str):
    with open(f'./data/report/{name_file}', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['id', 'nome', 'area', 'salario', 'bonus_percentual', 'bonus_final']   # Definindo colunas fixas/campos do nosso CSV, onde serão armazenados os dados.
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for dados in clean_data:

            csv_writer.writerow({"id": dados['id'],
                                "nome": dados['nome'],
                                "area": dados['area'],
                                "salario": dados['salario'],
                                "bonus_percentual": dados['bonus_percentual'],
                                "bonus_final": dados['bonus_final']})
            
    print(f"File: '{name_file}' Criado após a etapa de limpeza de dados em './data/report/{name_file}'")