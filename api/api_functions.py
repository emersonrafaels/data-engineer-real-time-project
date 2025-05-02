import requests
from loguru import logger

def get_weather_data(latitude, longitude, api_key):
    """
    Faz uma requisição à API Tomorrow.io para obter dados meteorológicos em tempo real.

    Args:
        latitude (float): Latitude da localização.
        longitude (float): Longitude da localização.
        api_key (str): Chave de API para autenticação.

    Returns:
        dict: Dados meteorológicos em formato JSON, ou None em caso de erro.
    """
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={api_key}"
    headers = {"accept": "application/json"}

    logger.info("Enviando requisição para a API Tomorrow.io.")
    try:
        response = requests.get(url, headers=headers)
        logger.info(f"Resposta recebida com status code: {response.status_code}")

        if response.status_code == 200:
            logger.success("Dados meteorológicos obtidos com sucesso.")
            return response.json()
        else:
            logger.error(
                f"Erro na requisição: {response.status_code}, mensagem: {response.json().get('message', '')}"
            )
            return None
    except requests.RequestException as e:
        logger.exception(f"Erro ao tentar se conectar à API: {e}")