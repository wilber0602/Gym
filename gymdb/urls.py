from django.urls import path
from . import views

urlpatterns = [
    path('panelUsuario/', views.panel_usuario, name='panelUsuario'),
    path('panelcoach/', views.panel_coach, name='panelcoach'),
    path('paneladmin/', views.panel_admin, name='paneladmin'),
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('gestion-calorica/', views.gestion_Calorica, name='gestion_calorica'),
    path('reportes/', views.reportes, name='reportes'),
    path('rutinas/', views.crear_rutinas, name='crear_rutinas'),
    path('finanzas/', views.finanzas, name='finanzas'),
    path('asignar-rutinas/', views.asignar_rutinas, name='asignar_rutinas'),
    path('progreso/', views.ver_progreso, name='ver_progreso'),
    path('asistencia/', views.registrar_asistencia, name='registrar_asistencia'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
