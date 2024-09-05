from pathlib import Path
from starlette.config import Config
config = Config(".env")

ENV = config("RUNTIME_ENV", cast=str, default="docker")

if ENV == "local":
    BASE_DIR = Path(__file__).parent.parent.resolve()
elif ENV == "docker":
    BASE_DIR = "/app"

RESOURCES_DIR = Path(BASE_DIR, "resources")
RESOURCES_DIR = 'app/'
YOLO_CONF_LEVEL = 0.6
YOLO_MODEL_PATH = Path(RESOURCES_DIR, 'yolo/best.pt')