from pathlib import Path
from starlette.config import Config
config = Config(".env")


RESOURCES_DIR = "resources"
YOLO_CONF_LEVEL = 0.6
YOLO_MODEL_PATH = Path(RESOURCES_DIR, 'best.pt')