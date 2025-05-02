from loguru import logger

def initialize_logger(log_file="weather_logs.log", log_level="INFO"):
    """
    Inicializa o logger com configurações padrão.

    Args:
        log_file (str): Caminho para o arquivo de log.
        log_level (str): Nível de log (ex: "INFO", "DEBUG", "ERROR").
    """
    logger.add(
        log_file,
        rotation="1 MB",
        level=log_level,
        format="{time} {level} {message}",
    )
    logger.info("Logger inicializado com sucesso.")