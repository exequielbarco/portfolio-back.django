import os
from .base import *

ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    from .prod import *
else:
    from .dev import *
