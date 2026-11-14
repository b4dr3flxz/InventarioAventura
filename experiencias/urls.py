from django.urls import path
from experiencias import views

urlpatterns = [
    path('categorias/', views.listarCategorias, name='ListaCategorias'),
    path('categorias/crear/', views.registrarCategoria, name='crearCategoria'),
    path('categorias/editar/<int:id>/', views.editarCategoria, name='editarCategoria'),
    path('categorias/eliminar/<int:id>/', views.eliminarCategoria, name='eliminarCategoria'),

    path('gestion/', views.listarExperiencias, name='ListaExperiencias'),
    path('gestion/crear/', views.registrarExperiencia, name='crearExperiencia'),
    path('gestion/editar/<int:id>/', views.editarExperiencia, name='editarExperiencia'),
    path('gestion/eliminar/<int:id>/', views.eliminarExperiencia, name='eliminarExperiencia'),
    path('gestion/estado/<int:id>/', views.cambiarEstadoExperiencia, name='cambiarEstadoExperiencia'),
    path('detalle/<int:id>/', views.detalleExperiencia, name='detalleExperiencia'),

    path('catalogo/', views.catalogo, name='catalogo'),
    path('reservar/<int:id>/', views.reservarExperiencia, name='reservarExperiencia'),
    path('mis-reservas/', views.misReservas, name='misReservas'),
    path('reserva/confirmar/<int:id>/', views.confirmarPago, name='confirmarPago'),
    path('reserva/cancelar/<int:id>/', views.cancelarReserva, name='cancelarReserva'),
    path('reserva/valorar/<int:id>/', views.valorarExperiencia, name='valorarExperiencia'),
    path('reservas-globales/', views.listarReservasAdmin, name='ListaReservasAdmin'),
]