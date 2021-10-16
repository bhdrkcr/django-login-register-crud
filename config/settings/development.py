# Third Party
import dj_database_url

# Local Folder
from .base import *

DEBUG = True

DATABASES["default"] = dj_database_url.config(default=config("SQL_URL"))

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": "",
}
