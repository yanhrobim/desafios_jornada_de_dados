from read_raw_file import read_csv_file
from clean_data import clean_data
from create_relatorio_individual import load_relatorio_final
from create_kpis import create_kpis_json_file

def pipeline():
    funcionários_csv = './data/raw/funcionarios.csv'
    read_file = read_csv_file(funcionários_csv)
    clean = clean_data(read_file)
    create_relatorio_individual = load_relatorio_final(clean_data=clean, name_file="relatorio_individual.csv")
    create_kpis_json_file(relatorio_individual=clean, path_to_kpis_json='./data/kpis/kpis.json')


if __name__ == "__main__":
    pipeline()