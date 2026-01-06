# Add Regras de Validação aos Dados.
from read_raw_file import read_csv_file
import re

read = read_csv_file(path_csv_file='./data/raw/funcionarios.csv')
clean_data = []

for linha in read:
        if not linha['nome'] == '':         # Filtro para remover linhas que possuem nome = ''.
                                            # No desafio, pedem que o relatorio_individual (o que iremos criar) somente possua registros válidos seguindo as Regras de Validação.
            clean_data.append(linha)
            
            encontrar_numero_string = re.findall(r'-?\d*\.?\d+', linha['nome'])
            res = [float(number) if "." in number else int(number) for number in encontrar_numero_string]
            for number in res:
                  nome_numero = re.sub(r'\d+', '', linha['nome'])

                  print(nome_numero)

print(clean_data)
                    

                  






