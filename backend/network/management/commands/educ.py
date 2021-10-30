import logging

from django.core.management.base import BaseCommand

from network.logic.tree import tree

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--size', default=0)
        parser.add_argument('--jobs', default=1, help='Количество работ. Для максимального количества -1.')

    def handle(self, *args, **options):
        size = int(options.get('size'))
        n_jobs = int(options.get('jobs'))
        tree(size=size, n_jobs=n_jobs)
