from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from cuentas import forms
from core.views import obtener_perfil


class SignUpView(CreateView):
    form_class = forms.RegistroTuristaForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def miPerfil(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    form = forms.PerfilForm(instance=perfil)
    if request.method == 'POST':
        form = forms.PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('perfil'))
    data = {'form': form, 'perfil': perfil}
    return render(request, 'cuentas/perfil.html', data)


def listarUsuarios(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    usuarios = User.objects.all()
    data = {'usuarios': usuarios, 'perfil': perfil}
    return render(request, 'cuentas/usuarios.html', data)


def registrarUsuario(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    form = forms.UsuarioAdminForm()
    if request.method == 'POST':
        form = forms.UsuarioAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaUsuarios'))
    data = {'form': form, 'titulo': 'Registrar Usuario', 'perfil': perfil}
    return render(request, 'cuentas/formularioUsuario.html', data)


def editarUsuario(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    usuario_obj = get_object_or_404(User, id=id)
    form = forms.UsuarioAdminForm(instance=usuario_obj)
    if request.method == 'POST':
        form = forms.UsuarioAdminForm(request.POST, instance=usuario_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaUsuarios'))
    data = {'form': form, 'titulo': 'Editar Usuario', 'perfil': perfil}
    return render(request, 'cuentas/formularioUsuario.html', data)


def eliminarUsuario(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    perfil = obtener_perfil(request.user)
    if perfil.rol != 'Administrador':
        return HttpResponseRedirect(reverse('dashboard'))
    usuario_obj = get_object_or_404(User, id=id)
    if usuario_obj.id != request.user.id:
        usuario_obj.delete()
    return HttpResponseRedirect(reverse('ListaUsuarios'))