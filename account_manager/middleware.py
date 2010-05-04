# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

class AccountManagerMiddleware:
    def process_response(self, request, response):
        try:
            current_site = Site.objects.get_current()
            url = "http://%s%s" % (current_site, reverse('amcd'))
            response['X-Account-Management'] = url
            if request.user.is_authenticated():
                response['X-Account-Management-Status'] = 'active; name="%s"' % (request.user.username)
            else:
                response['X-Account-Management-Status'] = 'none; token="%s"' % request.META["CSRF_COOKIE"]
        except:
            pass
        return response
