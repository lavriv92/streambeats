import os
from djang.conf import settings


def get_upload_path(instance, filename):
    path = ''
    profiles = settings.IMAGE_PROFILES
    if hasattr(instance, image):
        image_profile = profiles[instance.image.profile]
        path = os.path.join(path, image_profile['folder'])
        profiles = image_profile['profiles']


def get_image_profiles():
    return ((key, key) for key in settings.IMAGE_PROFILES.keys())
