from django.contrib.staticfiles.storage import staticfiles_storage
from jinja2 import contextfunction

@contextfunction
def staticfile(context, path=''):
    return staticfiles_storage.url(path)


context_functions = ( staticfile, )
