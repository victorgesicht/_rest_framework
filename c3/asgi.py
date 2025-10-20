import os
from configurations.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c3.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_asgi_application()


