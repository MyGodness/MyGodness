from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from models import MyGodnessUser

class MyGodnessUserForm(forms.ModelForm):
    def __init__(self, user_id, *args, **kwargs):
        super(MyGodnessUserForm, self).__init__(*args, **kwargs)
        self.instance.user_id = user_id
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = MyGodnessUser
        fields = ('gender', 'photo', 'motto', 'major', 'school')

    def save(self):
        userInfo, create = MyGodnessUser.objects.get_or_create(user_id=self.instance.user_id)
        if not create:
            userInfo.motto = self.cleaned_data['motto']
            userInfo.photo = self.cleaned_data['photo']
            userInfo.gender = self.cleaned_data['gender']
            userInfo.major = self.cleaned_data['major']
            userInfo.school = self.cleaned_data['school']
            userInfo.save()
        else:
            userInfo.motto = self.cleaned_data['motto']
            userInfo.photo = self.cleaned_data['photo']
            userInfo.gender = self.cleaned_data['gender']
            userInfo.major = self.cleaned_data['major']
            userInfo.school = self.cleaned_data['school']
            userInfo.save()

'''    def save(self):
        user_id = self.instance.user_id
        super(MyGodnessUserForm, self).save()'''





