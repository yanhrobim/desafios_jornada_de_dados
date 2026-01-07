# Add Regras de Validação aos Dados.
from read_raw_file import read_csv_file
import re

read = read_csv_file(path_csv_file='./data/raw/funcionarios.csv')
clean_data = {}

for linha in read:
      if not linha['nome'] == '':         # Filtro para remover linhas que possuem nome = ''.
                                          # No desafio, pedem que o relatorio_individual (o que iremos criar) 
                                          # somente possua registros válidos seguindo as Regras de Validação.
                  
            nome_numero =re.sub(r'\d+', '', linha['nome'])  # re.sub faz a função de um replace, 
                                                            # com um código regex encontra um número na string e 
                                                            # substitui por '', uma string vázia, "apagando" o número da string.
            
            linha.update({'nome': nome_numero.lstrip().rstrip()}) # Garantindo que os nomes que forem limpos 
                                                                  # as strings não contenham espaços depois da limpeza, 
                                                                  # com lstrip() caso o número fosse no começo do nome 
                                                                  # e com rstrip() caso o número estivesse no fim.


                    

                  






