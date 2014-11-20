from codecs import open
import os

from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, 'VERSION')) as f:
    VERSION = f.read().strip()

setup(
    name='django-premailer',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    license='MIT',
    version = VERSION,
    description = 'Django template tag that turns CSS blocks into style attributes using premailer.',
    author = 'Alex Hayes',
    author_email = 'alex@alution.com',
    url = 'https://github.com/alexhayes/django-premailer',
    download_url = 'https://github.com/alexhayes/django-premailer/tarball/%s' % VERSION,
    keywords = ['premailer', 'inline css', 'django', 'templatetag', 'html', 'lxml', 'email', 'mail', 'style'],
   
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
         
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Software Development :: Libraries :: Python Modules",
         
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
         
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
    ],
    
    include_package_data=True,
    install_requires=['premailer'],
)