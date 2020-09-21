from django.db import models
from django.urls import reverse


class News(models.Model):
    news_title = models.CharField(max_length=200, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    pub_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Картинка')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('one_news', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    cat_title = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
