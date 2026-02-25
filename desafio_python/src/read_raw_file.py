import csv

def read_csv_file(path_csv_file: str):
    csv_file = open(path_csv_file, mode='r+', newline='', encoding='utf-8')
    data = csv.DictReader(csv_file, delimiter=",")     # Lendo o CSV importando o método (csv), uma lib própria e disponibilizada pelo python.
                                                       # DictReader retorna nossos dados CSV em chave-valor, cada coluna sendo reconhecida como chave e os dados de colunas(individualmente) valor.
                                                       # A variável delimiter é adicionada ao código para indicar o caractere que separa as colunas uma das outras no nosso CSV sendo a ","(Vírgula). 
    return list(data)
