from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from learning_logs import views
from user.forms import LoginForm
from user.forms import CadastroForm
from django.contrib.auth import authenticate, login, logout

class CadastroView(View):

    def get(self, request):
        data = {'form': CadastroForm()}
        return render(request, 'cadastro.html', data)


    def post(self, request):
        form = CadastroForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            

            user = User.objects.create_user(
            username=username, password=password)

            if user:
                return redirect('index')

        data = {'form': form}

        return render(request, 'cadastro.html', data)

class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user:
            
                login(request, user)
                return redirect('index')

        data = {'form': form}

        return render(request, 'login.html', data)

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')

