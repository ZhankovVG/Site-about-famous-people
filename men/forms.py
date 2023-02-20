from .models import *
from django.forms import ModelForm, TextInput, Textarea, ValidationError, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class MenCreateForm(ModelForm):
    class Meta:
        model = Men
        fields = [
            'title', 'slug', 'content', 'photo', 'cat',
        ]

        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-post',
                'placeholder' : 'Заголовок'
            }),
            'content' : Textarea(attrs={
                'class' : 'form-post',
                'placeholder' : 'Текст статьи',
            }),
            'slug' : TextInput(attrs={
                'class' : 'form-post',
                'placeholder' : 'Url',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError ('Длина привышает 200 символов')
        return title


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
