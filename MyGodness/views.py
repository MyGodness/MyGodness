from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from users.models import MyGodnessUser as my

from auth.views import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        userInfo = my.objects.get(user_id = self.request.user.id)
        context['motto'] = userInfo.motto
        context['first_name'] = userInfo.first_name
        context['last_name'] = userInfo.last_name
        context['email'] = userInfo.email
        context['photo'] = userInfo.photo
        context['gender'] = userInfo.gender
        context['school'] = userInfo.school
        context['major'] = userInfo.major
        return context

