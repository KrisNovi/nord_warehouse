from django.db import models
from django.utils.translation import gettext_lazy as _


class Unit(models.Model):
    class Status(models.TextChoices):
        INSTOCK = 'INSTOCK', _('На складе')
        OUTOFSTOCK = 'OUTOFSTOCK', _('Нет на складе')

    class Vendor(models.TextChoices):
        ABB = 'ABB', _('ABB')
        Danfoss = 'Danfoss', _('Danfoss')
        VACON = 'VACON', _('VACON')
        ONI = 'ONI', _('ONI')
        Schneider = 'Schneider', _('Schneider')

    serial = models.CharField(
        max_length=250,
        verbose_name='Серийный номер',
        unique=True
    )
    code = models.CharField(
        max_length=250,
        verbose_name='Артикул',
        unique=False
    )
    vendor = models.CharField(
        max_length=250,
        verbose_name='Вендор',
        choices=Vendor.choices,
        default=Vendor.ABB,
        unique=False,
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    status = models.CharField(
        max_length=20,
        verbose_name='Статус',
        choices=Status.choices,
        default=Status.INSTOCK,
    )
    date_in = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
    )
    date_out = models.DateField(
        verbose_name='Дата отгрузки со склада',
        blank=True,
        null=True,
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )

    def is_in_stock(self):
        return self.status in {
            self.Status.INSTOCK,
            self.Status.OUTOFSTOCK,
        }

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Единицы оборудования'

    def __str__(self):
        return self.serial