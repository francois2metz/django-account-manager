# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

class AccountManagerMiddleware:
    def process_response(self, request, response):
        try:
            url = "%s://%s%s" % (request.META['wsgi.url_scheme'], request.META['HTTP_HOST'], reverse('amcd'))
            link = "<%s>; rel=\"acct-mgmt\"" % url
            response['Link'] = link
            if request.user.is_authenticated():
                response['X-Account-Management-Status'] = 'active; name="%s"' % (request.user.username)
            else:
                response['X-Account-Management-Status'] = 'none; token="%s"' % request.META["CSRF_COOKIE"]
        except:
            pass
        return response
