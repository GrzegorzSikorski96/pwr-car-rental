from django.core.management.base import BaseCommand

from core.initializers.group_initializer import GroupInitializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        GroupInitializer().initialize()
