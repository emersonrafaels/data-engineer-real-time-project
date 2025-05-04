import sys
import json
from pathlib import Path

import pytest
from unittest.mock import patch, MagicMock

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.config import settings
from lambda_function import lambda_handler
