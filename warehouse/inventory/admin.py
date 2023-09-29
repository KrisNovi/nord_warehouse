from django.contrib import admin

from .models import Unit

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'serial',
        'code',
        'vendor',
        'description',
        'status',
        # 'date_in',
        'date_out',
        'comment'
    )
    empty_value_display = "-"