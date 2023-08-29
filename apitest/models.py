from django.db import models


class Gem(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название камня')

    def __str__(self):
        return self.name


class Client(models.Model):
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    spent_money = models.PositiveIntegerField(verbose_name='Спущенные деньги')
    gems = models.ManyToManyField(Gem, verbose_name='Камни', blank=True, null=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    customer = models.CharField(
        max_length=50,
        verbose_name='Заказчик',
    )
    item = models.CharField(
        max_length=50,
        verbose_name='Камень',
    )
    total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Стоимость',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
    )
    date = models.DateTimeField(
        verbose_name='Дата',
    )

    def __str__(self):
        return self.customer

