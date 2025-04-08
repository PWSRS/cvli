from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    CidadeListView, CidadeCreateView,
    CidadeUpdateView, CidadeDeleteView,
    OcorrenciaListView, OcorrenciaCreateView,
    OcorrenciaUpdateView, OcorrenciaDeleteView,
    OcorrenciaDetailView,
    TipoCreateView, TipoListView,
    TipoUpdateView, TipoDeleteView,
    OrcrimListView, OrcrimCreateView,
    OrcrimUpdateView, OrcrimDeleteView,
    CausaFatoListView,
    CausaFatoCreateView,
    CausaFatoUpdateView,
    CausaFatoDeleteView,
    MeioEmpregadoListView,
    MeioEmpregadoCreateView,
    MeioEmpregadoUpdateView,
    MeioEmpregadoDeleteView,
    # e assim por diante...
)

urlpatterns = [
    # Ocorrências
    path('', OcorrenciaListView.as_view(), name='ocorrencia_list'),
    path('nova/', OcorrenciaCreateView.as_view(), name='ocorrencia_create'),
    path('<int:pk>/', OcorrenciaDetailView.as_view(), name='ocorrencia_detail'),
    path('<int:pk>/editar/', OcorrenciaUpdateView.as_view(), name='ocorrencia_edit'),
    path('<int:pk>/excluir/', OcorrenciaDeleteView.as_view(), name='ocorrencia_delete'),
      # Tipos
    path('tipos/', TipoListView.as_view(), name='tipo_list'),
    path('tipos/novo/', TipoCreateView.as_view(), name='tipo_create'),
    path('tipos/<int:pk>/editar/', TipoUpdateView.as_view(), name='tipo_update'),
    path('tipos/<int:pk>/excluir/', TipoDeleteView.as_view(), name='tipo_delete'),

    # Cidades
    path('cidades/', CidadeListView.as_view(), name='cidade_list'),
    path('cidades/nova/', CidadeCreateView.as_view(), name='cidade_create'),
    path('cidades/<int:pk>/editar/', CidadeUpdateView.as_view(), name='cidade_update'),
    path('cidades/<int:pk>/excluir/', CidadeDeleteView.as_view(), name='cidade_delete'),
    
    # MEIO EMPREGADO
    path('meios/', MeioEmpregadoListView.as_view(), name='meioempregado_list'),
    path('meios/novo/', MeioEmpregadoCreateView.as_view(), name='meioempregado_create'),
    path('meios/<int:pk>/editar/', MeioEmpregadoUpdateView.as_view(), name='meioempregado_update'),
    path('meios/<int:pk>/excluir/', MeioEmpregadoDeleteView.as_view(), name='meioempregado_delete'),

]


urlpatterns += [
    path('orcrins/', OrcrimListView.as_view(), name='orcrim_list'),
    path('orcrins/nova/', OrcrimCreateView.as_view(), name='orcrim_create'),
    path('orcrins/<int:pk>/editar/', OrcrimUpdateView.as_view(), name='orcrim_update'),
    path('orcrins/<int:pk>/excluir/', OrcrimDeleteView.as_view(), name='orcrim_delete'),
    path('causasfato/', CausaFatoListView.as_view(), name='causafato_list'),
    path('causasfato/nova/', CausaFatoCreateView.as_view(), name='causafato_create'),
    path('causasfato/<int:pk>/editar/', CausaFatoUpdateView.as_view(), name='causafato_update'),
    path('causasfato/<int:pk>/excluir/', CausaFatoDeleteView.as_view(), name='causafato_delete'),
    path('importar/', views.ImportarDadosView.as_view(), name='importar_dados'),
    # Importação de dados
    path('importar/', views.ImportarDadosView.as_view(), name='importar_dados'),
    path('exportar/', views.ExportarDadosView.as_view(), name='exportar_dados'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]
