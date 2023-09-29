# Generated by Django 3.2.21 on 2023-09-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Единица оборудования', 'verbose_name_plural': 'Единицы оборудования'},
        ),
        migrations.AlterField(
            model_name='unit',
            name='date_out',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отгрузки со склада'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.CharField(choices=[('INSTOCK', 'На складе'), ('OUTOFSTOCK', 'Нет на складе')], default='INSTOCK', max_length=20, verbose_name='Статус'),
        ),
    ]
