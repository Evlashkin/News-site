from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from captcha.fields import CaptchaField
import re

from .models import News


#Подключение CKEditor
class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=(forms.TextInput(
        attrs={'class': 'form-control'})))
    password = forms.CharField(label='Пароль', widget=(forms.PasswordInput(
        attrs={'class': 'form-control'})))


class UserRegisterForm(UserCreationForm, CaptchaField):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=(forms.TextInput(
        attrs={'class': 'form-control'})))
    email = forms.EmailField(label='Адрес электронной почты E-mail', widget=(forms.EmailInput(
        attrs={'class': 'form-control'})))
    password1 = forms.CharField(min_length=8, label='Пароль', widget=(forms.PasswordInput(
        attrs={'class': 'form-control'})))
    password2 = forms.CharField(min_length=8, label='Подтверждение пароля', widget=(forms.PasswordInput(
        attrs={'class': 'form-control'})))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'content', 'category']
        widgets = {
            'news_title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    # Кастомный валидатор
    def clean_news_title(self):
        title = self.cleaned_data['news_title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема сообщения', max_length=150,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(label='Текст сообщения',
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    cc_myself = forms.BooleanField(required=False)
