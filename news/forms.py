from django import forms
from django.core.exceptions import ValidationError
import re

from .models import News


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
    message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    cc_myself = forms.BooleanField(required=False)
