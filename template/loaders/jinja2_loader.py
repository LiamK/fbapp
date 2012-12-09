import sys
import os
from django.template.loader import BaseLoader
from django.template import TemplateDoesNotExist
from django.utils.importlib import import_module
from django.core import urlresolvers
from django.conf import settings
import jinja2
from template.loaders.jinja2_funcs import context_functions

# This code is borrowed from django.template.loaders.app_directories
# At compile time, cache the 'jinja_templates' directories to search.
fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
app_jinja_template_dirs = []
for app in settings.INSTALLED_APPS:
    try:
        mod = import_module(app)
    except ImportError, e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
    template_dir = os.path.join(os.path.dirname(mod.__file__), 'jinja_templates')
    if os.path.isdir(template_dir):
        app_jinja_template_dirs.append(template_dir.decode(fs_encoding))

# It won't change, so convert it to a tuple to save memory.
app_jinja_template_dirs = tuple(app_jinja_template_dirs)


class Template(jinja2.Template):
    def render(self, context):
        # flatten the Django Context into a single dictionary.
        context_dict = {}
        for d in context.dicts:
            context_dict.update(d)
        return super(Template, self).render(context_dict)

class Loader(BaseLoader):
    is_usable = True

    template_dirs = app_jinja_template_dirs + settings.JINJA_TEMPLATE_DIRS
    env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dirs),
            )
    env.template_class = Template

    # These are available to all templates.
    env.globals['url_for'] = urlresolvers.reverse
    env.globals['MEDIA_URL'] = settings.MEDIA_URL
    env.globals['STATIC_URL'] = settings.STATIC_URL

    # Add custom functions
    for cf in context_functions:
        env.globals[cf.__name__] = cf

    def load_template(self, template_name, template_dirs=None):
        try:
            template = self.env.get_template(template_name)
        except jinja2.TemplateNotFound:
            raise TemplateDoesNotExist(template_name)
        return template, template.filename
