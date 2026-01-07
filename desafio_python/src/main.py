from read_raw_file import read_csv_file
from clean_data import clean_data

def pipeline():
    funcionários_csv = './data/raw/funcionarios.csv'
    read_file = read_csv_file(funcionários_csv)
    clean = clean_data(read_file)


if __name__ == "__main__":
    pipeline()