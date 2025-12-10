from .base import *
import os
from django.core.exceptions import ImproperlyConfigured

STATIC_ROOT = BASE_DIR / "staticfiles"


def get_env_var(name: str) -> str:
    """
    Get the environment variable or raise an error.
    In prod we do NOT want silent defaults.
    """
    try:
        return os.environ[name]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {name} environment variable")


SECRET_KEY = get_env_var("SECRET_KEY")

DEBUG = get_env_var("DEBUG")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_var("DB_NAME"),
        "USER": get_env_var("DB_USER"),
        "PASSWORD": get_env_var("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

ALLOWED_HOSTS = get_env_var("ALLOWED_HOSTS").split(",")

CSRF_TRUSTED_ORIGINS = [
    origin.strip() for origin in get_env_var("CSRF_TRUSTED_ORIGINS").split(",")
]
