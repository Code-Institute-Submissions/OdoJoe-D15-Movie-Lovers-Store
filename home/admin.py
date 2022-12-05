from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    ordering = ('username',)


admin.site.register(Subscriber, SubscriberAdmin)
