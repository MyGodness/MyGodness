from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from models import MyGodnessUser

class MyGodnessUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyGodnessUserForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = MyGodnessUser
        fields = ('gender', 'photo', 'motto', 'major', 'school')

    def save(self):
        pass
