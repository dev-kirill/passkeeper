# -*- coding: utf-8 -*-
import os, sys
#project directory
sys.path.insert(0, '/home/s/slyuznta/passkeeper/passkeeper')
sys.path.insert(1, '/home/s/slyuznta/.local/lib/python3.4/site-packages')
#project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passkeeper.settings')
#start server
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()