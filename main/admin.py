from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = ("created_date",)
    list_display = ('name', 'mobile', 'text')
    ordering = ('created_date',)