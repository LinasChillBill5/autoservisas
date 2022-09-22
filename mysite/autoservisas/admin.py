from django.contrib import admin
from .models import Automobilio_modelis, Automobilis, Uzsakymas, Uzsakymo_eilute, Paslauga


class UzsakymoEiluteInline(admin.TabularInline):
    model = Uzsakymo_eilute
    can_delete = False
    extra = 0


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("data", "automobilis_ID")
    inlines = [UzsakymoEiluteInline]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("klientas", "automobilio_modelis_ID", "valstyb_nr", "vin_kodas")
    list_filter = ("klientas", "automobilio_modelis_ID")
    search_fields = ("valstybinis_nr", "vin_kodas")


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "kaina")

class Uzsakymo_eiluteAdmin(admin.ModelAdmin):
    list_display =("automobilis_ID", "status")


# Register your models here.
from .models import Automobilio_modelis, Automobilis, Uzsakymas, Uzsakymo_eilute, Paslauga

admin.site.register(Automobilio_modelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Uzsakymo_eilute)
admin.site.register(Paslauga, PaslaugaAdmin)
