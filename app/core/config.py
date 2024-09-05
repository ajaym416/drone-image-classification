from starlette.config import Config 
from starlette.datastructures import Secret
import os

config = Config(".env")
PROJECT_NAME = "Drone image classification"
VERSION = "1.0.0"

SECRET_KEY = config("SECRET_KEY", cast = Secret, default="CHANGEME")
