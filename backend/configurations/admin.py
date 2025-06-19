from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Configuration

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('configurationId', 'remark')