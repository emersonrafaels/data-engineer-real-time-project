import json
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
        return None


def print_json(data):
    """
    Exibe um JSON formatado no console.

    Args:
        data (dict): Dados em formato JSON.
    """
    logger.info("Exibindo dados formatados no console.")
    print(json.dumps(data, indent=4))


def main():
    """
    Função principal que define os parâmetros e executa o fluxo do programa.
    """
    latitude = -29.6846
    longitude = -51.1419
    api_key = "Ml1Az34K8d4KxiXmbQ1Wcq4Me8DeK1x6"

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
    logger.add(
        "weather_logs.log",
        rotation="1 MB",
        level="INFO",
        format="{time} {level} {message}",
    )
    main()
