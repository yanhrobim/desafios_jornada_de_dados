# Add Regras de Validação aos Dados.
import re
from read_raw_file import read_csv_file



def clean_data(read_csv_file):

      clean_data = []

      for linha in read_csv_file:

            if not linha['nome'] == '':         # Filtro para remover linhas que possuem nome = ''.
                                                # No desafio, pedem que o relatorio_individual (o que iremos criar) 
                                                # somente possua registros válidos seguindo as Regras de Validação.
                        

                  nome_numero = re.sub(r'\d+', '', linha['nome'])  # re.sub faz a função de um replace, 
                                                                  # com um código regex que encontra dígitos numéricos na string e 
                                                                  # substitui por '', uma string vázia, "apagando" o número da string.
                  
                  linha.update({'nome': nome_numero.lstrip().rstrip()}) # Garantindo que os nomes que forem limpos 
                                                                        # as strings não contenham espaços depois da limpeza, 
                                                                        # com lstrip() caso o número fosse no começo do nome 
                                                                        # e com rstrip() caso o número estivesse no fim.

                  if not linha['bonus_percentual'] == 'abc' and not linha['bonus_percentual'] == 'xyz':  # Condição/Filtro pode ser quebrado facilmente se fosse outros caracteres, mas lidando com o funcionarios.csv em especifíco é o mais rápido e simples de se fazer.
                  

                        cleaned_value = re.sub(r'[^0-9.]', '', linha['bonus_percentual']) 
                        # Este código Regex é o nosso filtro juntamente com o comando sub(), o código encontra todo tipo de
                        # caractere, aqueles dados neste campo que possuem algum caractere sem ser digito numérico ou '.'
                        #  ele substitui/"apaga" com ''(string vazia). Retornando apenas os números em formato float.

                        linha.update({'bonus_percentual': cleaned_value})

                        bonus_base = 1000
                        bonus_final = bonus_base + int(linha['salario']) * float(linha['bonus_percentual'])

                        linha.update({'bonus_final': f'{bonus_final}'})

                        clean_data.append(linha)


      return clean_data

                  






