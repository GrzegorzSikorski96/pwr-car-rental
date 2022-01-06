from core.initializers.group_initializer import GroupInitializer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        GroupInitializer().initialize()
