from loguru import logger

from config.config import settings

def initialize_logger():
    """
    Inicializa o logger com configurações obtidas do Dynaconf.
    """
    logger.add(
        settings.get("log_file"),  # Caminho do arquivo de log definido no Dynaconf
        rotation="1 MB",  # Rotação do arquivo de log
        level=settings.get("log_level"),  # Nível de log definido no Dynaconf
        format="{time} {level} {message}",
    )
    logger.info("Logger inicializado com sucesso.")
