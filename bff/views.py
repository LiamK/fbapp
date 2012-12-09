# Create your views here.
import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt

# NOTE: from inside the application, you can directly import the file
from django_facebook import exceptions as facebook_exceptions, \
    settings as facebook_settings
from django_facebook.api import get_persistent_graph, FacebookUserConverter, \
    require_persistent_graph, get_facebook_graph
from django_facebook.connect import CONNECT_ACTIONS, connect_user
from django_facebook.utils import next_redirect, get_registration_backend,\
    replication_safe, to_bool, error_next_redirect
from django_facebook.decorators import (facebook_required,
                                        facebook_required_lazy)
from open_facebook.utils import send_warning
from open_facebook import exceptions as open_facebook_exceptions
from django.shortcuts import redirect
from ssl import SSLError
from urllib2 import URLError

from django.http import HttpResponse
from django.conf import settings
from jinja2 import FileSystemLoader, Environment

#from coffin.shortcuts import render_to_response

logger = logging.getLogger(__name__)


template_dirs = getattr(settings,'JINJA_TEMPLATE_DIRS')
default_mimetype = getattr(settings, 'DEFAULT_CONTENT_TYPE')
env = Environment(loader=FileSystemLoader(template_dirs))

from django.core.context_processors import csrf
def render_to_response(request, filename, context={},mimetype=default_mimetype):
    token = csrf(request)
    print token
    context.update(token)
    template = env.get_template(filename)
    rendered = template.render(**context)
    return HttpResponse(rendered,mimetype=mimetype)


#@facebook_required_lazy()
def friends(request):
    '''
    '''
    fields="id,name,gender,relationship_status,location,interested_in,picture"
    if request.method == 'GET':
        context = { 'friends':[], 'paging':'' }
        return render_to_response(request, 'facebook.html', context)
    else: 
        print request.POST
        gender = request.POST.get('gender')
        status = request.POST.get('status')
        print gender, status
        fb = get_facebook_graph(request)
        limit = 5000
        response = fb.get('me/friends', fields=fields, limit=limit)
        paging = response.pop('paging')
        data = response.pop('data')
        print data[0]
        friends = filter(lambda f: True if gender == 'all' else f.get('gender', '') == gender, data)
        friends = filter(lambda f: f.get('relationship_status', '') == status, friends)
        #friends = filter(lambda f: f['relationship_status'] == status, friends)
        context = { 'friends':friends, 'paging':paging }

        return render_to_response(request, 'facebook.html', context)


