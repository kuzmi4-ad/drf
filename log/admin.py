from django.contrib import admin
from .models import Log
# Register your models here.

class LogAdmin(admin.ModelAdmin):
    # Вид в админке, фильтр/поля
    list_display = ['ip', 'URI', 'responceCode', 'userAgent']
    list_filter = ['URI', 'responceCode']
    search_fields = ['ip', 'userAgent']

admin.site.register(Log, LogAdmin)

