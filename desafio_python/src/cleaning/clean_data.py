# Add Regras de Validação aos Dados.
from src.ingestion.read_raw_file import read_csv_file
import re

def clean_data(read_csv_file):

      print("Começando a limpeza nos dados brutos :)")

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

                  linha_bonus_percentual = re.search(r'^[+-]?\d+\.\d+$|^\d+$', linha['bonus_percentual'])
                  # Utilização do módulo re (Regex) disponibilizado pelo Python, servindo nesta linha como principal filtro para aplicar uma regra de negócio, conter SOMENTE dados numéricos (float / int) na coluna de 'bonus_percentual'. Visando posteriormente fazer o cálculo de Bônus Final.
                  # O código encontra dentro dos dados da coluna 'bonus_percentual' somente valores numéricos, a lógica seria como: Pode ser negativos ou positivos, Pode ser float ou int, Pode ser somente número.
                  # Uma observação importante é que nesta parte do código teriamos como resposta valores numéricos negativos, não combinando para o cálculo de 'bonus_final', MAS que será executado mais uma etapa de filtragem no código para limpeza de caractéres. (Logicamente pensando que: Valores negativos de 'bonus_percentual' seriam erros de digitação, não que o Funcionário não possuí bônus.)

                  if linha_bonus_percentual: # Caso tentasse float(linha['bonus_percentual']) geraria erro por conta de haver valores strings na coluna, como 'xyz'. Esta intervenção sendo o principal motivo para o filtro acima.
                  

                        cleaned_value = re.sub(r'[^0-9.]', '', linha['bonus_percentual']) 
                        # Este código Regex é o nosso filtro juntamente com o comando sub(), o código encontra todo tipo de
                        # caractere, aqueles dados neste campo que possuem algum caractere sem ser digito numérico ou '.'
                        #  ele substitui/"apaga" com ''(string vazia). Retornando apenas os números em formato float.

                        linha.update({'bonus_percentual': cleaned_value})

                        bonus_base = 1000
                        bonus_final = bonus_base + int(linha['salario']) * float(linha['bonus_percentual'])

                        linha.update({'bonus_final': f'{round(bonus_final, 2)}'})

                        clean_data.append(linha)

      print(f"Limpeza de dados no arquivo CSV executada, dados limpos para KPIs!\n")

      return clean_data