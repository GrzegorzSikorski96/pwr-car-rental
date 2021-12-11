import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.db.backends.mysql.base import DatabaseWrapper


class Command(BaseCommand):
    NUMBER_OF_ATTEMPTS = 10

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')

        for i in range(0, self.NUMBER_OF_ATTEMPTS):
            try:
                database_connection: DatabaseWrapper = connections['default']
                database_connection.ensure_connection()
                break
            except OperationalError:
                if i == self.NUMBER_OF_ATTEMPTS - 1:
                    raise Exception('Database is not available')
                self.stdout.write('Database unavailable, waiting...(%d/%d)' % (i, self.NUMBER_OF_ATTEMPTS))
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS('Database available'))
