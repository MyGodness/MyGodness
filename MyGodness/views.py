from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from auth.views import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

