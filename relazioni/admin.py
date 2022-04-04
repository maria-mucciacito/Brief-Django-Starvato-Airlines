from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Fly)
admin.site.register(Aircraft)
admin.site.register(Personale)
admin.site.register(Manutenzione)
admin.site.register(Utent)
admin.site.register(Posto)
admin.site.register(Prenotazione)

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    search_fields = ('identification', 'name')