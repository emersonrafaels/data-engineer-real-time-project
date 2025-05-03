import json

import boto3
from dynaconf import settings
from loguru import logger

# Cliente do Kinesis
kinesis_client = boto3.client("kinesis", 
                              region_name=settings.get("kinesis_region"))


def send_to_kinesis(data):
    """
    Envia dados para o Amazon Kinesis.

    Args:
        data (dict): Dados a serem enviados.
    """
    try:
        logger.info("Preparando os dados para envio ao Kinesis.")

        # Converte os dados para JSON
        json_data = json.dumps(data)
        logger.debug(f"Dados convertidos para JSON: {json_data}")

        # Envia os dados para o Kinesis
        response = kinesis_client.put_record(
            StreamName=settings.get("kinesis_stream_name"),  # Nome do stream
            Data=json_data,
            PartitionKey="partitionkey",  # Chave de partição, pode ser qualquer valor
        )

        logger.info(f"Dados enviados com sucesso para o Kinesis. Resposta: {response}")
        return response

    except Exception as e:
        logger.error(f"Erro ao enviar dados para o Kinesis: {e}")
        raise
