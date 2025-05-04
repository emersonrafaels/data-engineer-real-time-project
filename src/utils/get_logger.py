import sys
from pathlib import Path

from loguru import logger

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from config_project.config import settings

def initialize_logger():
    """
    Inicializa o logger com configurações obtidas do Dynaconf.
    """
    try:
        # Remove todos os handlers existentes
        logger.remove()
        logger.debug("Handlers existentes removidos.") 
    
        logger.add(
            settings.get("log_file"),  # Caminho do arquivo de log definido no Dynaconf
            rotation="1 MB",  # Rotação do arquivo de log
            level=settings.get("log_level"),  # Nível de log definido no Dynaconf
            format="{time} {level} {message}",
        )
        logger.info("Logger inicializado com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao inicializar o logger: {e}")

