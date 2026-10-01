from django.contrib import admin
from .models import compliments


@admin.register(compliments)
class RunComp(admin.ModelAdmin):
    list_display=('text', 'created_at')

