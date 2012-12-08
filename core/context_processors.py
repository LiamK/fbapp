from collections import OrderedDict
from urllib import quote, urlopen
try: import json
except ImportError: import simplejson as json
from django.conf import settings

TW = 'http://%s:%s/webservice.php' % (settings.TERAWURFL_HOST, settings.TERAWURFL_PORT)

CAPABILITIES = (
    'brand_name',
    'device_claims_web_support',
    'device_os',
    'device_os_version',
    'is_tablet',
    'is_wireless_device',
    'marketing_name',
    'model_extra_info',
    'model_name',
    'resolution_height',
    'resolution_width',
    'physical_screen_height',
    'physical_screen_width',
)

def device(request):
    #device_dict = request.session.get('device')
    device_dict = None
    if not device_dict:
        device_dict = dict(device = _get_wurfl_device(request))
        request.session['device'] = device_dict
    return device_dict
    
def _get_wurfl_device(request):    
    if settings.USE_TERAWURFL == False: return {}
    REQUEST_PARAMS = '|'.join(CAPABILITIES)
    try:
        user_agent = unicode(request.META['HTTP_USER_AGENT'])
    except KeyError:
	user_agent = 'DO_NOT_MATCH_GENERIC_WEB_BROWSER'

    get_request = '?format=json&ua=%s&search=%s' % (quote(user_agent), REQUEST_PARAMS)
    response = urlopen(TW + get_request).read()
    response_obj = json.loads(response)
    errors = response_obj['errors']
    if errors: raise ValueError(errors)
    device = response_obj['capabilities']
    device['remote_addr'] = request.META.get('REMOTE_ADDR')
    device = OrderedDict(sorted(device.items(), key=lambda t: t[0]))

    return device
