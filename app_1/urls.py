from app_1 import views
from django.urls import path

urlpatterns = [
    #path("", views.inicio, name="Inicio"),
    path('', views.bienvenido, name='bienvenido'),
    path('proyectos/', views.listar_proyectos, name='listar_proyectos'),
    path('proyectos/nuevo/', views.nuevo_proyecto, name='nuevo_proyecto'),
    path('proyectos/buscar/', views.buscar_proyecto, name='buscar_proyecto'),
    path('habilidades/', views.listar_habilidades, name='listar_habilidades'),
    path('habilidades/nueva/', views.nueva_habilidad, name='nueva_habilidad'),
    path('educacion/', views.listar_educacion, name='listar_educacion' ),
    path('educacion/nueva', views.nueva_educacion, name='nueva_educacion'),
    path('experiencia', views.listar_experiencia, name='listar_experiencia'),
    path('listar_experiencia/nueva/', views.nueva_experiencia, name='nueva_experiencia'),
]
