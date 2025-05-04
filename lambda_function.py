import sys
import json
from pathlib import Path

from loguru import logger

sys.path.append(str(Path(__file__).resolve().parent))

from config.config import settings
from src.api.api_functions import get_weather_data
from src.kinesis.put_records import send_to_kinesis
from src.utils.get_logger import initialize_logger

# Inicializa o logger no momento da inicialização do Lambda
initialize_logger()


def lambda_handler(event, context):
    """
    Handler do AWS Lambda para obter dados meteorológicos e enviá-los ao Kinesis.

    Args:
        event (dict): Evento de entrada do Lambda.
        context (object): Contexto de execução do Lambda.

    Returns:
        dict: Resposta com status e mensagem.
    """

    try:
        logger.info("Iniciando o Lambda para obter dados meteorológicos.")

        # Obtém as configurações do Dynaconf
        latitude = settings.latitude
        longitude = settings.longitude
        api_key = settings.api_key

        # Obtém os dados meteorológicos
        weather_data = get_weather_data(latitude, longitude, api_key)

        # Verifica se os dados foram retornados
        if weather_data:
            logger.info("Dados meteorológicos obtidos com sucesso.")
            send_to_kinesis(weather_data)  # Envia os dados para o Kinesis
            return {
                "statusCode": 200,
                "body": json.dumps(
                    {"message": "Dados enviados para o Kinesis com sucesso."}
                ),
            }
        else:
            logger.warning("Nenhum dado meteorológico foi retornado.")
            return {
                "statusCode": 404,
                "body": json.dumps(
                    {"message": "Nenhum dado meteorológico foi retornado."}
                ),
            }

    except Exception as e:
        logger.error(f"Erro ao processar o Lambda: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps(
                {"message": "Erro interno no servidor.", "error": str(e)}
            ),
        }
