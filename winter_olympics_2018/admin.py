from django.contrib import admin
from .models import Country

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('rank', 'noc', 'short', 'gold', 'silver', 'bronze', 'total')

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


admin.site.register(Country, CountryAdmin)


admin.site.site_header = "MOODY'S ANALYTICS"
admin.site.site_title = "MOODY'S ANALYTICS Portal"
admin.site.index_title = "Welcome to MOODY'S ANALYTICS Portal"