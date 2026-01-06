from src.read_raw_file import read_csv_file

def pipeline():
    funcionários_csv = './data/raw/funcionarios.csv'
    read_file = read_csv_file(funcionários_csv)


if __name__ == "__main__":
    pipeline()