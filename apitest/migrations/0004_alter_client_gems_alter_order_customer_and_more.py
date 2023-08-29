# Generated by Django 4.2.4 on 2023-08-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0003_gem_remove_client_gems_alter_client_spent_money_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gems',
            field=models.ManyToManyField(blank=True, to='apitest.gem', verbose_name='Камни'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=50, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.CharField(max_length=50, verbose_name='Камень'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость'),
        ),
    ]
