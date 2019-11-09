from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    # Aqui vão suas urls

    path('sair/', auth_views.LogoutView.as_view(
        template_name = 'cadastros/base.html',
        ), name="logout"),

    path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
        template_name = 'usuarios/login.html',
        extra_context = {
            'titulo': 'Alterar senha atual', 
            'botao': 'Alterar',
            'classe': 'btn-success'
            },
        success_url = reverse_lazy('index')
        ), name="alterar-senha"),


]
