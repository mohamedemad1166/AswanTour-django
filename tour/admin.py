from django.contrib import admin
from .models import Tours


# Register your models here.

class ToursAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tour_name',)}
    list_display = ('tour_name', 'price', 'created_date', 'category')


admin.site.register(Tours,ToursAdmin)
