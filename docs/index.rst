.. Django Account Manager documentation master file, created by
   sphinx-quickstart on Mon May  3 00:03:36 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Account Manager's documentation!
=======================================

Contents:

.. toctree::
   :maxdepth: 2

Experimental implementation of `Account Management and Session Identification <https://wiki.mozilla.org/Labs/Weave/Identity/Account_Manager/Spec/Latest#Contents_of_the_Account_Management_Control_Document>`_ by Mozilla Labs.


Install
-------

        pip install django-account-manager

Configuration
-------------

In your ``settings.py``::

        INSTALLED_APPS = (
            ...,
            'django.contrib.sites',
            'django.contrib.auth',
            'account_manager'
        )

        MIDDLEWARE_CLASSES = (
            ...,
            'account_manager.middleware.AccountManagerMiddleware',
        )
   
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

