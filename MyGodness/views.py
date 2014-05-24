from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

class IndexView(TemplateView):
    template_name = 'index.html'

