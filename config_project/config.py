from pathlib import Path

from dynaconf import Dynaconf

dir_root = Path(__file__).resolve().parent  # Caminho do diretório raiz do projeto

settings = Dynaconf(
    settings_files=[str(Path(dir_root, "settings.yaml")), 
                    str(Path(dir_root, ".secrets.yaml"))], # Arquivos de configuração
                    environments=True,  # Permite o uso de ambientes
                    load_dotenv=True,  # Carrega variáveis de ambiente do .env
)

# settings = Dynaconf(settings_files=["settings.yaml", ".secrets.yaml"],
#                     environments=True, 
#                     load_dotenv=True)

print(settings.get("latitude"))
print(Path(dir_root, "settings.yaml"))