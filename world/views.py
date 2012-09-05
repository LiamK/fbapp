# Create your views here.
from collections import OrderedDict
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.conf import settings
from models import WorldBorder	

try: import json
except ImportError: import simplejson as json
from urllib import quote, urlopen

def index(request):
    qs = WorldBorder.objects.all().order_by('name')
    content = { 'qs':qs }
    
    return render(request, 'world/index.html', content)

