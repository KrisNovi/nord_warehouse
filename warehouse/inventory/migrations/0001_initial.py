# Generated by Django 3.2.21 on 2023-09-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=250, unique=True, verbose_name='Серийный номер')),
                ('code', models.CharField(max_length=250, verbose_name='Артикул')),
                ('vendor', models.CharField(max_length=250, verbose_name='Вендор')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('INSTOCK', 'На складе'), ('OUTOFSTOCK', 'Нет на складе')], default='INSTOCK', max_length=20)),
                ('date_in', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_out', models.DateTimeField(verbose_name='Дата отгрузки со склада')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
    ]
