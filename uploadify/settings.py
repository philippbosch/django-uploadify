from django.conf import settings
MEDIA_URL = getattr(settings, 'MEDIA_URL', '')
STATIC_URL = getattr(settings, 'STATIC_URL', '')

# Uploadify root folder path, relative to MEDIA_ROOT
UPLOADIFY_PATH = getattr(settings, 'UPLOADIFY_PATH', '%s%s' % (STATIC_URL, 'js/uploadify/'))

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = getattr(settings, 'UPLOADIFY_UPLOAD_PATH', '%s%s' % (MEDIA_URL, 'uploads/'))
