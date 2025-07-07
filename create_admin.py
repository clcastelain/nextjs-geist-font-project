from django.core.management import execute_from_command_line
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
execute_from_command_line([
    'manage.py',
    'shell',
    '-c',
    'from django.contrib.auth.models import User; User.objects.create_superuser("admin", "claudinei@bonssens.com.br", "123abc*") if not User.objects.filter(username="admin").exists() else print("Admin user already exists")'
])
