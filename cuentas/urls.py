from django.urls import path
from cuentas import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('perfil/', views.miPerfil, name='perfil'),
    path('usuarios/', views.listarUsuarios, name='ListaUsuarios'),
    path('usuarios/crear/', views.registrarUsuario, name='crearUsuario'),
    path('usuarios/editar/<int:id>/', views.editarUsuario, name='editarUsuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminarUsuario, name='eliminarUsuario'),
]