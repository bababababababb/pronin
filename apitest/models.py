from django.db import models


class Gem(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название камня')


class Client(models.Model):
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    spent_money = models.PositiveIntegerField(verbose_name='Спущенные деньги')
    gems = models.ManyToManyField(Gem, verbose_name='Камни')

class Order(models.Model):
    customer = models.CharField(max_length=50, verbose_name='Заказчик', blank=True)
    item = models.CharField(max_length=50, verbose_name='Камень', blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', blank=True)
    date = models.DateTimeField(verbose_name='', blank=True)