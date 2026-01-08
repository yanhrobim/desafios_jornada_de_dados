from read_raw_file import read_csv_file
from clean_data import clean_data
from create_relatorio_individual import load_relatorio_final

def pipeline():
    funcionários_csv = './data/raw/funcionarios.csv'
    read_file = read_csv_file(funcionários_csv)
    clean = clean_data(read_file)
    create_relatorio_individual = load_relatorio_final(clean)


if __name__ == "__main__":
    pipeline()