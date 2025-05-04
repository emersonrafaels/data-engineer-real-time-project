import sys
from pathlib import Path

import pytest
from unittest.mock import patch, MagicMock

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.config import settings
from src.api.api_functions import get_weather_data

@pytest.fixture
def mock_response():
    """Mock para a resposta da API."""
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {"temperature": 25, "humidity": 80}
    return response


@patch("src.api.api_functions.requests.get")
def test_get_weather_data_success(mock_get, mock_response):
    """Teste para verificar o sucesso da função get_weather_data."""
    # Configura o mock para retornar uma resposta bem-sucedida
    mock_get.return_value = mock_response

    # Chama a função com parâmetros fictícios
    latitude = -29.6846
    longitude = -51.1419
    api_key = "fake_api_key"
    result = get_weather_data(latitude, longitude, api_key)

    # Verifica se a função retornou os dados esperados
    assert result == {"temperature": 25, "humidity": 80}
    mock_get.assert_called_once_with(
        f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={api_key}",
        headers={"accept": "application/json"},
    )


@patch("src.api.api_functions.requests.get")
def test_get_weather_data_error_status_code(mock_get):
    """Teste para verificar o comportamento quando a API retorna um erro."""
    # Configura o mock para retornar um status code de erro
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"message": "Invalid request"}
    mock_get.return_value = mock_response

    # Chama a função com parâmetros fictícios
    latitude = -29.6846
    longitude = -51.1419
    api_key = "fake_api_key"
    result = get_weather_data(latitude, longitude, api_key)

    # Verifica se a função retornou None em caso de erro
    assert result is None
    mock_get.assert_called_once()


@patch("src.api.api_functions.requests.get")
def test_get_weather_data_exception(mock_get):
    """Teste para verificar o comportamento quando ocorre uma exceção."""
    # Configura o mock para lançar uma exceção
    mock_get.side_effect = Exception("Erro de conexão")

    # Chama a função com parâmetros fictícios
    latitude = -29.6846
    longitude = -51.1419
    api_key = "fake_api_key"
    result = get_weather_data(latitude, longitude, api_key)

    # Verifica se a função retornou None em caso de exceção
    assert result is None
    mock_get.assert_called_once()