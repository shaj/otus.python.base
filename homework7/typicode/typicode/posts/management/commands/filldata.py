from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError, CommandParser


class Command(BaseCommand):
    help = "Fill database with data from jsonplaceholder.com"
    
    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write('My first command for Django project\n')
        return 'My first Django command COMPLETE'
    