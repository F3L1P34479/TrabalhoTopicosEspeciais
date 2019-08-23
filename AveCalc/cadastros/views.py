from django.shortcuts import render
# Importa todas as classes do models.py
from .models import *

# importa a função que vai chamar as urlspelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir uitlizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

#Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

#Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir um arquivo HTML normal
# (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # nome do arquivo que vai ser utilizado para renderizar esta
    # página/método/classe
    template_name = "cadastros/index.html"

class SobreView(TemplateView):
    template_name = "cadastros/sobre.html"

class ContatoView(TemplateView):
    template_name = "cadastros/contato.html"

class CurriculoView(TemplateView):
    template_name = "cadastros/curriculo.html"


#################INSERIR#####################

class EstadoCreate(LoginRequiredMixin,CreateView):
    # Define qual o modelo para essa classe, criando o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "cadastros/formulario.html"
    # Pra onde o usuario irá ser redirecionado depois de inserir um registro. Informe o nome
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulario?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)
        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado']

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context


class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-pessoas")
    fields = ['nome', 'email', 'fone']

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novas Pessoas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context

class RacaoCreate(LoginRequiredMixin, CreateView):
    model = Racao
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-racao")
    fields = ['nome', 'sigla']

    def get_context_data(self, *args, **kwargs):
        context = super(RacaoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Ração"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context

class EntradaCreate(LoginRequiredMixin, CreateView):
    model = Entrada
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-entradas")
    fields = ['dataChegada', 'peso', 'racao']

    def get_context_data(self, *args, **kwargs):
        context = super(EntradaCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Entrada de ração"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context

class MatrizCreate(LoginRequiredMixin, CreateView):
    model = Matriz
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-matrizes")
    fields = ['idade', 'loteMatriz']

    def get_context_data(self, *args, **kwargs):
        context = super(MatrizCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Matrizes"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context

class AviarioCreate(LoginRequiredMixin, CreateView):
    model = Aviario
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-aviario")
    fields = ['identificacao', 'localizacao', 'cidade',
    'largura', 'comprimento', 'capacidadeAlojamento', 'ventilacao']

    def get_context_data(self, *args, **kwargs):
        context = super(AviarioCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Aviarios"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context
#################EDITAR#####################


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    # Define qual o modelo para essa classe, criando o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "cadastros/formulario.html"
    # Pra onde o usuario irá ser redirecionado depois de inserir um registro. Informe o nome
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulario?
    fields = ['sigla', 'nome']

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado', 'descricao']

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-pessoas")
    fields = ['nome', 'email', 'fone']

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Pessoas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context

class RacaoUpdate(LoginRequiredMixin, UpdateView):
    model = Racao
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-racao")
    fields = ['nome', 'sigla']

    def get_context_data(self, *args, **kwargs):
        context = super(RacaoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Rações"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context

class EntradaUpdate(LoginRequiredMixin, UpdateView):
    model = Entrada
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-entradas")
    fields = ['dataChegada', 'peso', 'racao']

    def get_context_data(self, *args, **kwargs):
        context = super(EntradaUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Entradas de ração"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context

class MatrizUpdate(LoginRequiredMixin, UpdateView):
    model = Matriz
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-matrizes")
    fields = ['idade', 'loteMatriz']

    def get_context_data(self, *args, **kwargs):
        context = super(MatrizUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Matrizes"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context

class AviarioUpdate(LoginRequiredMixin, UpdateView):
    model = Aviario
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("listar-aviario")
    fields = ['identificacao', 'localizacao', 'cidade',
    'largura', 'comprimento', 'capacidadeAlojamento', 'ventilacao']

    def get_context_data(self, *args, **kwargs):
        context = super(AviarioUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Aviarios"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-warning"

        return context

#################DELETAR#####################

class EstadoDelete(LoginRequiredMixin, DeleteView):
    # Define qual o modelo para essa classe, criando o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "cadastros/formulario.html"
    # Pra onde o usuario irá ser redirecionado depois de inserir um registro. Informe o nome
    success_url = reverse_lazy("listar-estados")

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)
        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context


class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

class RacaoDelete(LoginRequiredMixin, DeleteView):
    model = Racao
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *args, **kwargs):
        context = super(RacaoDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

class EntradaDelete(LoginRequiredMixin, DeleteView):
    model = Entrada
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *args, **kwargs):
        context = super(EntradaDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

class MatrizDelete(LoginRequiredMixin, DeleteView):
    model = Matriz
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *args, **kwargs):
        context = super(MatrizDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

class AviarioDelete(LoginRequiredMixin, DeleteView):
    model = Aviario
    template_name = "cadastros/formulario.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *args, **kwargs):
        context = super(AviarioDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        return context

#################LISTAR#####################

#Vai gerar uma tela com uma lista de estados
class EstadoList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Estado
    #e o
    template_name = "cadastros/list_estado.html"

class CidadeList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Cidade
    #e o
    template_name = "cadastros/list_estado.html"

class PessoaList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Pessoa
    #e o
    template_name = "cadastros/list_estado.html"

class RacaoList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Matriz
    #e o
    template_name = "cadastros/list_estado.html"

class EntradaList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Entrada
    #e o
    template_name = "cadastros/list_estado.html"

class MatrizList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Matriz
    #e o
    template_name = "cadastros/list_estado.html"

class AviarioList(LoginRequiredMixin, ListView):
    #informa qual o modelo
    model = Aviario
    #e o
    template_name = "cadastros/list_estado.html"
