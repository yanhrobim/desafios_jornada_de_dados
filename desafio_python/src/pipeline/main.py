from src.ingestion.read_raw_file import read_csv_file
from src.cleaning.clean_data import clean_data
from src.analytics.create_relatorio_individual import load_relatorio_final
from src.analytics.create_kpis_json import create_kpis_json_file
from app.app import run_app
import os

def pipeline(path_raw_csv: str, clean_csv_filename: str, path_to_kpis_json: str):
    funcionários_csv = path_raw_csv
    read_file = read_csv_file(funcionários_csv)
    clean = clean_data(read_file)
    load_relatorio_final(clean_data=clean, name_file=clean_csv_filename)
    create_kpis_json_file(relatorio_individual=clean, path_to_kpis_json=path_to_kpis_json)
    run_app()
    os.system('python -m streamlit run app/app.py')

if __name__ == "__main__":
    pipeline(path_raw_csv="./data/raw/funcionarios.csv", clean_csv_filename="relatorio_individual.csv", path_to_kpis_json="./data/kpis/kpis.json")