import logging

from django.core.management.base import BaseCommand

from network.logic.text_analysis import text

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--size', default=0)
        parser.add_argument('--jobs', default=1, help='Количество работ. Для максимального количества -1.')

    def handle(self, *args, **options):
        text()