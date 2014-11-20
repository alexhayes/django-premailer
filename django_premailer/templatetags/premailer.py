from __future__ import absolute_import
from django import template
from django.utils.encoding import smart_unicode
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from premailer import Premailer

register = template.Library()

PREMAILER_OPTIONS = getattr(settings, 'PREMAILER_OPTIONS', {})

class PremailerNode(template.Node):
    def __init__(self, nodelist, filter_expressions):
        self.nodelist = nodelist
        self.filter_expressions = filter_expressions

    def render(self, context):
        rendered_contents = self.nodelist.render(context)
        kwargs = PREMAILER_OPTIONS.copy()
        
        for expression in self.filter_expressions:
            kwargs.update(base_url=expression.resolve(context, True))
        
        transformed = Premailer(rendered_contents, **kwargs).transform()
        return transformed

@register.tag
def premailer(parser, token):
    nodelist = parser.parse(('endpremailer',))

    # prevent second parsing of endpremailer
    parser.delete_first_token()

    args = token.split_contents()[1:]

    return PremailerNode(
        nodelist,
        [parser.compile_filter(arg) for arg in args])