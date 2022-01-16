from core.initializers.required_fixtures_initializer import RequiredFixturesInitializer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        RequiredFixturesInitializer().initialize()
