# -*- coding: utf-8 -*-
__version__ = (0, 2, 3, 'final', 0)

from django.core.exceptions import ImproperlyConfigured

try:
    from django_any.forms import any_form_field, any_form
    from django_any.models import any_field, any_model
except (ImportError, ImproperlyConfigured):
    pass
