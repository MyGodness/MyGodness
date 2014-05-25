from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import (
        CreateView,
        TemplateView,
        FormView,
)

from forms import (
        MyGodnessUserForm,
)
from models import (
        MyGodnessUser,
)


class PersonInfoView(FormView):
    template_name = 'users/login.html'
    model = MyGodnessUser
    form_class = MyGodnessUserForm

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super(PersonInfoView, self).get_context_data(**kwargs)
        context['usage'] = 'User Info'
        return context

