from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.utils import simplejson as json


def control_document(request):
    control = {
        "methods": {
            "username-password-form": {
                "connect": {
                    "method":"POST",
                    "path": reverse('signin'),
                    "params": {
                        "username":"username",
                        "password":"password",
                        "token" : 'csrfmiddlewaretoken',
                        }
                    },
                "disconnect": {
                    "method":"POST",
                    "path": reverse('signout')
                    },
                "sessionstatus": {
                    "method":"GET",
                    "path": reverse('session_status')
                    },
                }
            }
        }
    return HttpResponse(json.dumps(control))

def session_status(request):
    return HttpResponse('Session status')
