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
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('GUIA', 'Guía / Operador'), ('TURISTA', 'Turista / Cliente')], default='TURISTA', max_length=20)),
                ('telefono', models.CharField(blank=True, default='', max_length=20)),
                ('especialidad', models.CharField(blank=True, default='', help_text='Especialidad o certificación (aplicable a Guías ecoturísticos)', max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'Perfiles de Usuarios',
            },
        ),
    ]
