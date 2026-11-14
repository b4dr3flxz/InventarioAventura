from django.contrib import admin
from experiencias.models import Categoria, Experiencia, Inscripcion


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado']
    search_fields = ['nombre']
    list_filter = ['estado']


class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'creador', 'precio', 'cupo_maximo', 'fecha_hora', 'estado']
    search_fields = ['titulo', 'descripcion', 'creador__username']
    list_filter = ['categoria', 'estado']


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'experiencia', 'fecha_inscripcion', 'estado_pago', 'valoracion']
    search_fields = ['usuario__username', 'experiencia__titulo']
    list_filter = ['estado_pago', 'valoracion']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)