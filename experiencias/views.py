from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models.deletion import ProtectedError
from experiencias.models import Categoria, Experiencia, Inscripcion
from experiencias import forms
from core.views import obtener_perfil


def listarCategorias(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    categorias = Categoria.objects.all()
    data = {'categorias': categorias, 'perfil': perfil}
    return render(request, 'experiencias/categorias.html', data)


def registrarCategoria(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    form = forms.CategoriaRegistroForm()
    if request.method == 'POST':
        form = forms.CategoriaRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaCategorias'))
    data = {'form': form, 'titulo': 'Nueva Categoría', 'perfil': perfil}
    return render(request, 'experiencias/formularioCategoria.html', data)


def editarCategoria(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    categoria = get_object_or_404(Categoria, id=id)
    form = forms.CategoriaRegistroForm(instance=categoria)
    if request.method == 'POST':
        form = forms.CategoriaRegistroForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaCategorias'))
    data = {'form': form, 'titulo': 'Editar Categoría', 'perfil': perfil}
    return render(request, 'experiencias/formularioCategoria.html', data)


def eliminarCategoria(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    categoria = get_object_or_404(Categoria, id=id)
    try:
        categoria.delete()
    except ProtectedError:
        categoria.estado = False
        categoria.save()
    return HttpResponseRedirect(reverse('ListaCategorias'))


def listarExperiencias(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol == 'Administrador':
        experiencias = Experiencia.objects.all()
    elif perfil.rol == 'Guia':
        experiencias = Experiencia.objects.filter(creador=request.user)
    else:
        return HttpResponseRedirect(reverse('catalogo'))
    data = {
        'experiencias': experiencias,
        'perfil': perfil,
        'es_admin': perfil.rol == 'Administrador',
    }
    return render(request, 'experiencias/experiencias.html', data)


def registrarExperiencia(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol not in ['Administrador', 'Guia']:
        return HttpResponseRedirect(reverse('dashboard'))
    form = forms.ExperienciaRegistroForm()
    if request.method == 'POST':
        form = forms.ExperienciaRegistroForm(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.creador = request.user
            experiencia.save()
            return HttpResponseRedirect(reverse('ListaExperiencias'))
    data = {'form': form, 'titulo': 'Registrar Experiencia', 'perfil': perfil}
    return render(request, 'experiencias/formularioExperiencia.html', data)


def editarExperiencia(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol not in ['Administrador', 'Guia']:
        return HttpResponseRedirect(reverse('dashboard'))
    experiencia = get_object_or_404(Experiencia, id=id)
    if perfil.rol == 'Guia' and experiencia.creador != request.user:
        return HttpResponseRedirect(reverse('ListaExperiencias'))
    form = forms.ExperienciaRegistroForm(instance=experiencia)
    if request.method == 'POST':
        form = forms.ExperienciaRegistroForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaExperiencias'))
    data = {'form': form, 'titulo': 'Editar Experiencia', 'perfil': perfil}
    return render(request, 'experiencias/formularioExperiencia.html', data)


def eliminarExperiencia(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('ListaExperiencias'))
    experiencia = get_object_or_404(Experiencia, id=id)
    experiencia.delete()
    return HttpResponseRedirect(reverse('ListaExperiencias'))


def cambiarEstadoExperiencia(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol not in ['Administrador', 'Guia']:
        return HttpResponseRedirect(reverse('dashboard'))
    experiencia = get_object_or_404(Experiencia, id=id)
    if perfil.rol == 'Guia' and experiencia.creador != request.user:
        return HttpResponseRedirect(reverse('ListaExperiencias'))
    experiencia.estado = not experiencia.estado
    experiencia.save()
    return HttpResponseRedirect(reverse('ListaExperiencias'))


def detalleExperiencia(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    experiencia = get_object_or_404(Experiencia, id=id)
    if perfil.rol == 'Guia' and experiencia.creador != request.user:
        return HttpResponseRedirect(reverse('ListaExperiencias'))

    vistas = request.session.get('experiencias_vistas', [])
    if id not in vistas:
        vistas.append(id)
    request.session['experiencias_vistas'] = vistas[-5:]

    inscripciones = experiencia.inscripciones.all()
    ya_inscrito = Inscripcion.objects.filter(usuario=request.user, experiencia=experiencia).first()
    data = {
        'experiencia': experiencia,
        'inscripciones': inscripciones,
        'ya_inscrito': ya_inscrito,
        'perfil': perfil,
    }
    return render(request, 'experiencias/detalleExperiencia.html', data)


def catalogo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    categoria_id = request.GET.get('categoria')
    experiencias = Experiencia.objects.filter(estado=True, categoria__estado=True)
    if categoria_id:
        experiencias = experiencias.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.filter(estado=True)
    mis_ids = list(Inscripcion.objects.filter(usuario=request.user).values_list('experiencia_id', flat=True))
    data = {
        'experiencias': experiencias,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
        'mis_ids': mis_ids,
        'perfil': perfil,
    }
    return render(request, 'experiencias/catalogo.html', data)


def reservarExperiencia(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Turista':
        return HttpResponseRedirect(reverse('dashboard'))
    experiencia = get_object_or_404(Experiencia, id=id)
    if request.method == 'POST':
        existe = Inscripcion.objects.filter(usuario=request.user, experiencia=experiencia).exists()
        if not existe and experiencia.estado and experiencia.cupos_disponibles() > 0:
            Inscripcion.objects.create(
                usuario=request.user,
                experiencia=experiencia,
                estado_pago='Pendiente'
            )
    return HttpResponseRedirect(reverse('misReservas'))


def misReservas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Turista':
        return HttpResponseRedirect(reverse('dashboard'))
    reservas = Inscripcion.objects.filter(usuario=request.user)
    data = {'reservas': reservas, 'perfil': perfil}
    return render(request, 'experiencias/misReservas.html', data)


def confirmarPago(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if perfil.rol == 'Administrador' or inscripcion.usuario == request.user:
        if request.method == 'POST':
            inscripcion.estado_pago = 'Confirmado'
            inscripcion.save()
    if perfil.rol == 'Administrador':
        return HttpResponseRedirect(reverse('ListaReservasAdmin'))
    return HttpResponseRedirect(reverse('misReservas'))


def cancelarReserva(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if perfil.rol == 'Administrador' or inscripcion.usuario == request.user:
        if request.method == 'POST':
            inscripcion.delete()
    if perfil.rol == 'Administrador':
        return HttpResponseRedirect(reverse('ListaReservasAdmin'))
    return HttpResponseRedirect(reverse('misReservas'))


def valorarExperiencia(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if inscripcion.usuario != request.user or inscripcion.estado_pago != 'Confirmado':
        return HttpResponseRedirect(reverse('misReservas'))
    form = forms.ValoracionForm(instance=inscripcion)
    if request.method == 'POST':
        form = forms.ValoracionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('misReservas'))
    data = {'form': form, 'inscripcion': inscripcion, 'perfil': perfil}
    return render(request, 'experiencias/formularioValoracion.html', data)


def listarReservasAdmin(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    reservas = Inscripcion.objects.all()
    data = {'reservas': reservas, 'perfil': perfil}
    return render(request, 'experiencias/reservasAdmin.html', data)