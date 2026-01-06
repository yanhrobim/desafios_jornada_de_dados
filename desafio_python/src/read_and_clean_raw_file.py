import csv

def read_csv_file(path_csv_file: str):
    with open(path_csv_file, newline='') as csv_file:
        data = csv.DictReader(csv_file)     # Lendo o CSV importando o método (csv), uma lib própria e disponibilizada pelo python.
                                        # DictReader retorna nossos dados CSV em chave-valor, cada coluna sendo reconhecida como chave e os dados de colunas(individualmente) valor. 
        for linha in data:
            print(linha)

if __name__ == "__main__":
    read_csv_file(path_csv_file='./data/raw/funcionarios.csv')