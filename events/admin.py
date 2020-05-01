from django.contrib import admin
from .models import *


class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'type', 'creatorName')


admin.site.register(Events, EventsAdmin)

