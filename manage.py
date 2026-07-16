#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# import pymysql
# pymysql.install_as_MySQLdb()

def main():
    """Run administrative tasks."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(current_dir, 'apps'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BugAndTestcase.settings')
    try:
        from django.core.management import execute_from_command_line
        import django
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
