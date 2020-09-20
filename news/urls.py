from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<int:category_id>/', GetCategory.as_view(), name='category'),
    path('news/<int:news_id>/', one_news, name='one_news'),
    path('add-news/', add_news, name='add_news'),
    path('send-message/', send_message, name='send_message'),
    path('thanks/', thanks, name='thanks'),
]
