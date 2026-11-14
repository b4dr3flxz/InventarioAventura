from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Activa')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=0, help_text='Precio en CLP', max_digits=10)),
                ('cupo_maximo', models.PositiveIntegerField(default=10)),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y Hora de Realización')),
                ('estado', models.BooleanField(default=True, verbose_name='Ruta Activa')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='experiencias', to='experiencias.categoria')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencias_creadas', to=settings.AUTH_USER_MODEL, verbose_name='Guía / Creador')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ['fecha_hora'],
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateTimeField(auto_now_add=True)),
                ('estado_pago', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado')], default='Pendiente', max_length=20)),
                ('valoracion', models.PositiveSmallIntegerField(blank=True, help_text='Calificación de 1 a 5 estrellas', null=True)),
                ('comentario', models.TextField(blank=True, default='')),
                ('experiencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to='experiencias.experiencia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to=settings.AUTH_USER_MODEL, verbose_name='Turista')),
            ],
            options={
                'verbose_name': 'Inscripción / Reserva',
                'verbose_name_plural': 'Inscripciones y Reservas',
                'ordering': ['-fecha_inscripcion'],
                'unique_together': {('usuario', 'experiencia')},
            },
        ),
    ]
