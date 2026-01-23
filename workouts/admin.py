from django.contrib import admin

# Register your models here.
from .models import Exercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('name',)
    date_hierarchy = 'created_at'