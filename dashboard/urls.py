from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastros/', views.cadastros, name='cadastros'),
   # CRUD Cliente
    path('cliente/', views.clientes, name='clientes'),
    path('cliente/add/', views.cliente_create, name='cliente_create'),
    path('cliente/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    
    path('processos/', views.processos, name='processos'),
    path('consultas/', views.consultas, name='consultas'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),

    # Agrupador Básico - Países
    path('basico/paises/', views.paises, name='paises'),
    path('basico/paises/add/', views.paises_create, name='pais_create'),
    path('basico/paises/<int:pk>/edit/', views.paises_update, name='pais_update'),
    path('basico/paises/<int:pk>/delete/', views.paises_delete, name='pais_delete'),

    # Agrupador Básico - Estados
    path('basico/estados/', views.estados, name='estados'),
    path('basico/estados/add/', views.estados_create, name='estado_create'),
    path('basico/estados/<int:pk>/edit/', views.estados_update, name='estado_update'),
    path('basico/estados/<int:pk>/delete/', views.estados_delete, name='estado_delete'),

    # Agrupador Básico - Cidades
    path('basico/cidades/', views.cidades, name='cidades'),
    path('basico/cidades/add/', views.cidades_create, name='cidade_create'),
    path('basico/cidades/<int:pk>/edit/', views.cidades_update, name='cidade_update'),
    path('basico/cidades/<int:pk>/delete/', views.cidades_delete, name='cidade_delete'),

    # CRUD Empresa
    path('empresa/', views.empresas, name='empresas'),
    path('empresa/add/', views.empresa_create, name='empresa_create'),
    path('empresa/<int:pk>/edit/', views.empresa_update, name='empresa_update'),
    path('empresa/<int:pk>/delete/', views.empresa_delete, name='empresa_delete'),

    # CRUD Estado Civil
    path('basico/estado-civil/', views.estados_civis, name='estados_civis'),
    path('basico/estado-civil/add/', views.estado_civil_create, name='estado_civil_create'),
    path('basico/estado-civil/<int:pk>/edit/', views.estado_civil_update, name='estado_civil_update'),
    path('basico/estado-civil/<int:pk>/delete/', views.estado_civil_delete, name='estado_civil_delete'),

    # CRUD Escolaridade
    path('basico/escolaridade/', views.escolaridades, name='escolaridades'),
    path('basico/escolaridade/add/', views.escolaridade_create, name='escolaridade_create'),
    path('basico/escolaridade/<int:pk>/edit/', views.escolaridade_update, name='escolaridade_update'),
    path('basico/escolaridade/<int:pk>/delete/', views.escolaridade_delete, name='escolaridade_delete'),

    # CRUD Objetivo
    path('basico/objetivos/', views.objetivos, name='objetivos'),
    path('basico/objetivos/add/', views.objetivo_create, name='objetivo_create'),
    path('basico/objetivos/<int:pk>/edit/', views.objetivo_update, name='objetivo_update'),
    path('basico/objetivos/<int:pk>/delete/', views.objetivo_delete, name='objetivo_delete'),

        # CRUD Estado Civil
    path('basico/beneficio-inss/', views.beneficios_inss, name='beneficios_inss'),
    path('basico/beneficio-inss/add/', views.beneficio_inss_create, name='beneficio_inss_create'),
    path('basico/beneficio-inss/<int:pk>/edit/', views.beneficio_inss_update, name='beneficio_inss_update'),
    path('basico/beneficio-inss/<int:pk>/delete/', views.beneficio_inss_delete, name='beneficio_inss_delete'),
]
