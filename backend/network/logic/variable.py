import os

from django.conf import settings

path_tree = os.path.join(os.path.dirname(settings.BASE_DIR), 'backend', 'network', 'trees', 'tree.joblib')
