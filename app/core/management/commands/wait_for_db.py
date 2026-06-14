"""wait for database to be available - a Django command"""

import time

from psycopg2 import OperationalError as PsycopgOpError
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


# generic empty command template
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except PsycopgOpError:
                self.stdout.write('Postgres not yet launched, waiting 1 second...')
                time.sleep(1)
            except OperationalError:
                self.stdout.write('Database is unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database now available!'))
