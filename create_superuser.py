from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='claudinei@bonssens.com.br',
            password='123abc*'
        )
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")

if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    django.setup()
    create_superuser()
