from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


class HomePage(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/homepage.html'

    def get_queryset(self):
        news = News.objects.filter(is_published=True)
        return news

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class GetCategory(ListView):
    model = News
    template_name = 'news/homepage.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GetCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class OneNews(DetailView):
    model = News
    template_name = 'news/one_news.html'
    context_object_name = 'title'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OneNews, self).get_context_data(**kwargs)
        context['count_view'] = count_view(self).count_view
        return context


def count_view(self):
    count_views = News.objects.get(pk=self.kwargs['pk'])
    count_views.count_view += 1
    count_views.save()
    return count_views


class NewNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'


# def index(request):
#     news = News.objects.filter(is_published=True).order_by('-pub_date')
#     template_name = 'news/index.html'
#     context = {
#         'title': 'Список новостей',
#         'news': news,
#     }
#     return render(request, template_name, context)


# def get_category(request, category_id):
#     news = News.objects.filter(is_published=True, category_id=category_id)
#     category = Category.objects.get(id=category_id)
#     template_name = 'news/categories.html'
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, template_name, context)

# def one_news(request, news_id):
#     news = News.objects.filter(id=news_id)
#     title = News.objects.get(id=news_id)
#     title.count_view += 1
#     title.save()
#     template_name = 'news/one_news.html'
#     context = {
#         'news': news,
#         'title': title,
#         'count_view': title.count_view
#     }
#     return render(request, template_name, context)


# def thanks(request):
#     return HttpResponse('<h1>Успешно!</h1>')


# def add_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
#
#
# def send_message(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid:
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             sender = form.cleaned_data['sender']
#             cc_myself = form.cleaned_data['cc_myself']
#
#             recipients = ['evlashkin@gmail.com', ]
#             if cc_myself:
#                 recipients.append(sender)
#
#             send_mail(subject, message, sender, recipients)
#             return redirect('thanks')
#     else:
#         form = ContactForm()
#     return render(request, 'news/contact.html', {'form': form})
