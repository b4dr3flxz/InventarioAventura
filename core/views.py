from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from cuentas.models import Perfil
from experiencias.models import Categoria, Experiencia, Inscripcion


def obtener_perfil(user):
    perfil, creado = Perfil.objects.get_or_create(user=user)
    mapa_roles = {
        'ADMINISTRADOR': 'Administrador',
        'GUIA': 'Guia',
        'TURISTA': 'Turista',
    }
    if perfil.rol in mapa_roles:
        perfil.rol = mapa_roles[perfil.rol]
        perfil.save()
    elif creado and user.is_superuser:
        perfil.rol = 'Administrador'
        perfil.save()
    return perfil


def home(request):
    experiencias = Experiencia.objects.filter(estado=True, categoria__estado=True)
    vistas_ids = request.session.get('experiencias_vistas', [])
    recientes = Experiencia.objects.filter(id__in=vistas_ids, estado=True)
    data = {
        'experiencias': experiencias,
        'recientes': recientes,
    }
    return render(request, 'home.html', data)


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    request.session['rol'] = perfil.rol
    request.session['usuario'] = request.user.username

    data = {
        'perfil': perfil,
        'rol': perfil.rol,
    }

    if perfil.rol == 'Administrador':
        data['total_usuarios'] = User.objects.count()
        data['total_categorias'] = Categoria.objects.count()
        data['total_experiencias'] = Experiencia.objects.count()
        data['total_reservas'] = Inscripcion.objects.count()
    elif perfil.rol == 'Guia':
        mis_experiencias = Experiencia.objects.filter(creador=request.user)
        mis_reservas = Inscripcion.objects.filter(experiencia__creador=request.user)
        data['total_mis_experiencias'] = mis_experiencias.count()
        data['total_visitantes'] = mis_reservas.count()
    else:
        mis_reservas = Inscripcion.objects.filter(usuario=request.user)
        data['total_mis_reservas'] = mis_reservas.count()
        data['reservas_confirmadas'] = mis_reservas.filter(estado_pago='Confirmado').count()

    return render(request, 'core/dashboard.html', data)