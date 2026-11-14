from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Guia', 'Guía / Operador'),
        ('Turista', 'Turista / Cliente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='Turista')
    telefono = models.CharField(max_length=20, blank=True, default='')
    especialidad = models.CharField(max_length=120, blank=True, default='')

    def rol_normalizado(self):
        mapa = {
            'ADMINISTRADOR': 'Administrador',
            'GUIA': 'Guia',
            'TURISTA': 'Turista',
        }
        return mapa.get(self.rol, self.rol)

    def nombre_rol(self):
        etiquetas = dict(self.ROLES)
        return etiquetas.get(self.rol_normalizado(), self.rol)

    def __str__(self):
        return f"{self.user.username} ({self.rol_normalizado()})"