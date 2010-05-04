.. Django Account Manager documentation master file, created by
   sphinx-quickstart on Mon May  3 00:03:36 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Account Manager's documentation!
=======================================

.. toctree::
   :maxdepth: 2

Experimental implementation of `Account Management and Session Identification <https://wiki.mozilla.org/Labs/Weave/Identity/Account_Manager/Spec/Latest>`_ by Mozilla Labs in `Django <http://www.djangoproject.com/>`_.

Features
--------

 * Connect
 * Disconnect
 * Handle CSRF Django protection
 * Handle sessionstatus

Requirements
------------

To get started, you'll need:
 * Django >= 1.2

Install
-------

        pip install django-account-manager

Configuration
-------------

In your ``settings.py``::

        INSTALLED_APPS = (
            ...,
            'django.contrib.auth',
            'account_manager',
        )

        MIDDLEWARE_CLASSES = (
            ...,
            'account_manager.middleware.AccountManagerMiddleware',
        )

In your ``urls.py``::

        urlpatterns = patterns('',
            ...,
            (r'amcd/', include('account_manager.urls')),
            (r'xxx/signin/', 'your.view', name='signin'),   # Needed
            (r'xxx/signout/', 'your.view', name='signout'), # Needed
            ...
        )

   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

