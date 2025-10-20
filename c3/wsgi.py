import os
from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c3.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')  # or your config class

application = get_wsgi_application()
