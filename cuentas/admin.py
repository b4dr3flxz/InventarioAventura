from django.contrib import admin
from cuentas.models import Perfil


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'rol', 'telefono', 'especialidad']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'especialidad']
    list_filter = ['rol']


admin.site.register(Perfil, PerfilAdmin)