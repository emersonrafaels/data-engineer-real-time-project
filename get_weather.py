import sys
import json
from pathlib import Path

from loguru import logger
from dynaconf import settings  # Importando as configurações do Dynaconf

# Adicionando a pasta pai ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from api.api_functions import get_weather_data
from utils.get_logger import initialize_logger  # Importando as configurações do Dynaconf

def print_json(data):
    """
    Exibe um JSON formatado no console.

    Args:
        data (dict): Dados em formato JSON.
    """
    logger.info("Exibindo dados formatados no console.")
    print(json.dumps(data, indent=4))
    
def send_data_to_kinesis(data):
    """
    Envia dados para o Amazon Kinesis.

    Args:
        data (dict): Dados a serem enviados.
    """
    logger.info("Enviando dados para o Amazon Kinesis.")
    # Aqui você implementaria a lógica para enviar os dados para o Kinesis
    pass


def main():
    """
    Função principal que define os parâmetros e executa o fluxo do programa.
    """
    latitude = settings.get("latitude")  # Obtendo latitude do Dynaconf
    longitude = settings.get("longitude")  # Obtendo longitude do Dynaconf
    api_key = settings.get("api_key")  # Obtendo chave da API do Dynaconf

    logger.info("Iniciando o programa para obter dados meteorológicos.")

    # Obtém os dados meteorológicos
    weather_data = get_weather_data(latitude, longitude, api_key)

    # Exibe os dados formatados, se disponíveis
    if weather_data:
        print_json(weather_data)
    else:
        logger.warning("Nenhum dado meteorológico foi retornado.")

    logger.info("Execução do programa finalizada.")


if __name__ == "__main__":
    initialize_logger()  # Configurando o logger com Dynaconf
    main()