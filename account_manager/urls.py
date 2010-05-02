from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    #(r'.well-known/host-meta', 'account_manager.views.host_meta'),
    (r'amcd', 'account_manager.views.control_document', {}, 'amcd'),
    (r'sessionstatus', 'account_manager.views.session_status', {}, 'session_status')
)
