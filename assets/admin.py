from django.contrib import admin
from .models import Vendor, Asset

admin.site.register(Vendor)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'model', 'borrowed_date', 'returned_date')