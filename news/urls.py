from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<int:category_id>/', GetCategory.as_view(), name='category'),
    path('news/<pk>/', OneNews.as_view(), name='one_news'),
    path('add-news/', NewNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    # path('send-message/', send_message, name='send_message'),
    # path('thanks/', thanks, name='thanks'),
]
