from django.contrib import admin
from .models import Stockitem, Format, Region, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

    ordering = ('pk',)


class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

    ordering = ('pk',)


class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

    ordering = ('pk',)


class StockitemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'region',
        'format',
        'genre',
        'price',
        'is_special_edition'
    )

    ordering = ('name',)


admin.site.register(Stockitem, StockitemAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Genre, GenreAdmin)


