from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Experiencia(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cupo_maximo = models.PositiveIntegerField(default=10)
    fecha_hora = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='experiencias')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiencias_creadas')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    def inscritos_count(self):
        return self.inscripciones.count()

    def cupos_disponibles(self):
        disponibles = self.cupo_maximo - self.inscritos_count()
        return max(0, disponibles)


class Inscripcion(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmado', 'Confirmado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscripciones')
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado_pago = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    valoracion = models.PositiveSmallIntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True, default='')

    class Meta:
        unique_together = ('usuario', 'experiencia')

    def __str__(self):
        return f"{self.usuario.username} - {self.experiencia.titulo}"
