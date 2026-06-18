from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('django-celery-beat-rest')
except PackageNotFoundError:
    pass
