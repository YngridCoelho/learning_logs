from django.urls import path

from .views import LoginView
from .views import CadastroView
from .views import LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('logout', LogoutView.as_view(), name='logout')
]