from setuptools import setup, find_packages

setup(
    name='django-account-manager',
    version='0.0.2',
    description='Experimental implementation of Account Management and Session Identification of Mozilla Labs',
    long_description=open('README.rst').read(),

    author='Francois de Metz',
    author_email='francois@2metz.fr',
    url='http://forge.2metz.fr/p/django-account-manager/',

    license='BSD',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

