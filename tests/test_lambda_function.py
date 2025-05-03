import json
import pytest
from unittest.mock import patch, MagicMock
from lambda_function import lambda_handler

@pytest.fixture
def mock_event():
    """Mock do evento de entrada do Lambda."""
    return {"key": "value"}

@pytest.fixture
def mock_context():
    """Mock do contexto do Lambda."""
    return MagicMock()

@patch("lambda_function.get_weather_data")
@patch("lambda_function.send_to_kinesis")
def test_lambda_handler_success(mock_send_to_kinesis, mock_get_weather_data, mock_event, mock_context):
    """Teste para verificar o sucesso do lambda_handler."""
    # Mockando o retorno da função get_weather_data
    mock_get_weather_data.return_value = {"temperature": 25, "humidity": 80}

    # Chamando o lambda_handler
    response = lambda_handler(mock_event, mock_context)

    # Verificando se os dados foram enviados para o Kinesis
    mock_send_to_kinesis.assert_called_once_with({"temperature": 25, "humidity": 80})

    # Verificando a resposta do Lambda
    assert response["statusCode"] == 200
    assert json.loads(response["body"])["message"] == "Dados enviados para o Kinesis com sucesso."

@patch("lambda_function.get_weather_data")
def test_lambda_handler_no_data(mock_get_weather_data, mock_event, mock_context):
    """Teste para verificar o comportamento quando nenhum dado é retornado."""
    # Mockando o retorno da função get_weather_data
    mock_get_weather_data.return_value = None

    # Chamando o lambda_handler
    response = lambda_handler(mock_event, mock_context)

    # Verificando a resposta do Lambda
    assert response["statusCode"] == 404
    assert json.loads(response["body"])["message"] == "Nenhum dado meteorológico foi retornado."

@patch("lambda_function.get_weather_data")
def test_lambda_handler_exception(mock_get_weather_data, mock_event, mock_context):
    """Teste para verificar o comportamento em caso de exceção."""
    # Mockando uma exceção na função get_weather_data
    mock_get_weather_data.side_effect = Exception("Erro simulado")

    # Chamando o lambda_handler
    response = lambda_handler(mock_event, mock_context)

    # Verificando a resposta do Lambda
    assert response["statusCode"] == 500
    assert "Erro interno no servidor." in json.loads(response["body"])["message"]
    assert "Erro simulado" in json.loads(response["body"])["error"]