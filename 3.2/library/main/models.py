from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=50, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Название произведения')
    year = models.PositiveSmallIntegerField(verbose_name='Год публикации')

    def __str__(self):
        return f'{self.author} - {self.title}'


class Order(models.Model):
    user_name = models.CharField(max_length=200, verbose_name='ФИО')
    days_count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество дней заказа')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    books = models.ManyToManyField(Book)

