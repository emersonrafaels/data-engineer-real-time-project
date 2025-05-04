import sys
import json
from pathlib import Path

import pytest
from unittest.mock import patch, MagicMock

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config_project.config import settings
from lambda_function import lambda_handler

def test_lambda():
    
    assert True, "Teste de exemplo para garantir que o pytest está funcionando."
    # Aqui você pode adicionar mais testes específicos para a função lambda_handler
