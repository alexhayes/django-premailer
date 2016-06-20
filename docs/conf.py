import pkg_resources
import sys
import os
import sphinx_rtd_theme

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_premailer.tests.testapp.settings')

this = os.path.dirname(os.path.abspath(__file__))


# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.join(this, os.pardir))

from django_premailer import __version__

# Monkey patch to get around https://github.com/sphinx-doc/sphinx/issues/1254

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              #'sphinx.ext.intersphinx',
              ]

templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = 'django-premailer'
copyright_holder = 'Alex Hayes'
copyright = u'2016, %s' % copyright_holder
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = '%sdoc' % project

latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project, copyright_holder, 'manual'),
]
man_pages = [
    ('index', project, u'%s Documentation' % project,
     [copyright_holder], 1)
]

version = __version__
release = version

# autodoc_default_flags = ['members', 'private-members', 'special-members',
#                          'undoc-members',
#                          'show-inheritance']

def autodoc_skip_member(app, what, name, obj, skip, options):
    exclusions = ('__weakref__',  # special-members
                  '__doc__', '__module__', '__dict__',  # undoc-members
                  )
    exclude = name in exclusions
    return skip or exclude

def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)


