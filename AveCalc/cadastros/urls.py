from django.urls import path

from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('principal/', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo"),

    #URLS de cadastros
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/tecnico/', TecnicoCreate.as_view(), name="cadastrar-tecnico"),
    path('cadastrar/granjeiro/', GranjeiroCreate.as_view(), name="cadastrar-granjeiro"),
    path('cadastrar/proprietario/', ProprietarioCreate.as_view(), name="cadastrar-proprietario"),
    path('cadastrar/racao/', RacaoCreate.as_view(), name="cadastrar-racao"),
    path('cadastrar/entrada/', EntradaCreate.as_view(), name="cadastrar-entrada"),
    path('cadastrar/matriz/', MatrizCreate.as_view(), name="cadastrar-matriz"),
    path('cadastrar/aviario/', AviarioCreate.as_view(), name="cadastrar-aviario"),

    #URLS de alterar cadastros
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/tecnico/<int:pk>/', TecnicoUpdate.as_view(), name="editar-tecnico"),
    path('editar/granjeiro/<int:pk>/', GranjeiroUpdate.as_view(), name="editar-granjeiro"),
    path('editar/proprietario/<int:pk>/', ProprietarioUpdate.as_view(), name="editar-proprietario"),
    path('editar/racao/<int:pk>/', RacaoUpdate.as_view(), name="editar-racao"),
    path('editar/entrada/<int:pk>/', EntradaUpdate.as_view(), name="editar-entrada"),
    path('editar/matriz/<int:pk>/', MatrizUpdate.as_view(), name="editar-matriz"),
    path('editar/aviario/<int:pk>/', AviarioUpdate.as_view(), name="editar-aviario"),

    #URLS de excluir cadastros
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/tecnico/<int:pk>/', TecnicoDelete.as_view(), name="excluir-tecnico"),
    path('excluir/granjeiro/<int:pk>/', GranjeiroDelete.as_view(), name="excluir-granjeiro"),
    path('excluir/proprietario/<int:pk>/', ProprietarioDelete.as_view(), name="excluir-proprietario"),
    path('excluir/racao/<int:pk>/', RacaoDelete.as_view(), name="excluir-racao"),
    path('excluir/entrada/<int:pk>/', EntradaDelete.as_view(), name="excluir-entrada"),
    path('excluir/matriz/<int:pk>/', MatrizDelete.as_view(), name="excluir-matriz"),
    path('excluir/aviario/<int:pk>/', AviarioDelete.as_view(), name="excluir-aviario"),

    #URLS de listar cadastros
    path('listar/estado/', EstadoList.as_view(), name="listar-estados"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidades"),
    path('listar/tecnico/', TecnicoList.as_view(), name="listar-tecnicos"),
    path('listar/granjeiro/', GranjeiroList.as_view(), name="listar-granjeiros"),
    path('listar/racao/', RacaoList.as_view(), name="listar-racao"),
    path('listar/entrada/', EntradaList.as_view(), name="listar-entradas"),
    path('listar/matriz/', MatrizList.as_view(), name="listar-matrizes"),
    path('listar/aviario/', AviarioList.as_view(), name="listar-aviario"),

    #URLS de detalhes
    path('ver/aviario/<int:pk>/', AviarioDetalhes.as_view(), name="detalhar-aviario"),
]
