from drfauth.settings.base import ALLOWED_HOSTS
from decouple import config


ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")


DEBUG = True
