import os
from django.conf import settings


def get_upload_path(path):
    return os.path.join(settings.UPLOADS_PATH, path)


def resize_image(path):
    pass
