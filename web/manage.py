#!./../env/bin python3
"""Django's command-line utility for administrative tasks."""
import sys
sys.path.insert(0, '/com.docker.devenvironments.code/crypto_wallet/')
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_wallet.settings')
django.setup()
import threading
from database.models import coins

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_wallet.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
