"Script de ingestão treinamento DPH"

import pandas as pd
import requests
import utils as utils
from dotenv import load_dotenv
from config import configs
import logging

load_dotenv()
config_file = configs
logging.basicConfig(level=logging.INFO)


def ingestion():
    """
    Função de ingestão dos dados
    Outputs: Salva base raw em local específico e retorna o nome do arquivo
    """

    logging.info("Iniciando a ingestão")
    api_url = configs["URL"]
    try:
        response = requests.get(api_url, timeout=10).json()
        data = response['results']
    except Exception as exception_error:
        utils.error_handler(exception_error, 'read_api', configs['path']['logs'])
    df = pd.json_normalize(data)
    cols = [s.replace('.', '_') for s in df.columns]
    df.columns = cols
    utils.save_mysql(df, "mysql", "cadastro_raw")
    #utils.save_folder(df, configs['path']['raw'])
    

def preparation():
    """
    Função de preparação dos dados: renomeia, tipagem, normaliza strings
    Arguments: file -> nome do arquivo raw
    Outputs: Salva base limpa em local específico
    """

    logging.info("Iniciando o saneamento")
    df = utils.read_mysql("mysql", "cadastro_raw")
    san = utils.Saneamento(df, config_file)
    san.select_rename()
    logging.info("Seleção de dados")
    df = san.tipagem()
    logging.info("Tipagem dos dados")
    #utils.save_folder(df, configs['path']['work'])
    utils.save_mysql(df, "mysql", "cadastro")
    logging.info("Dados salvos na camada work")
    

if __name__ == '__main__':
    ingestion()
    preparation()