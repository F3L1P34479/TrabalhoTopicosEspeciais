from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import UsuarioCreate


urlpatterns = [
    # Aqui vão suas urls
    path('registrar/', UsuarioCreate.as_view(), name="user-create"),

    path('sair/', auth_views.LogoutView.as_view(
        template_name = 'usuarios/login.html',
        ), name="logout"),

    path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
        template_name = 'usuarios/form.html',
        extra_context = {
            'titulo': 'Alterar senha atual', 
            'botao': 'Alterar',
            'classe': 'btn-success'
            },
        success_url = reverse_lazy('index')
        ), name="alterar-senha"),


]
