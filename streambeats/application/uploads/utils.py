import os
from djang.conf import settings


def get_upload_path():
    path = ''
    profiles = settings.IMAGE_PROFILES
    return 'uploads'


def get_image_profiles():
    return [(key, key) for key in settings.IMAGE_PROFILES.keys()]
