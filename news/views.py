from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import *
from .forms import *


def index(request):
    news = News.objects.filter(is_published=True).order_by('-pub_date')
    template_name = 'news/index.html'
    context = {
        'title': 'Список новостей',
        'news': news,
    }
    return render(request, template_name, context)


def get_category(request, category_id):
    news = News.objects.filter(is_published=True, category_id=category_id)
    category = Category.objects.get(id=category_id)
    template_name = 'news/categories.html'
    context = {
        'news': news,
        'category': category,
    }
    return render(request, template_name, context)


def one_news(request, news_id):
    news = News.objects.filter(id=news_id)
    title = News.objects.get(id=news_id)
    title.count_view += 1
    title.save()
    template_name = 'news/one_news.html'
    context = {
        'news': news,
        'title': title,
        'count_view': title.count_view
    }
    return render(request, template_name, context)


def thanks(request):
    return HttpResponse('<h1>Успешно!</h1>')


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})


def send_message(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['evlashkin@gmail.com', ]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'news/contact.html', {'form': form})
