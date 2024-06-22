from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from .forms import SignUpForm, LoginForm


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # ユーザーを作成した後にログインする
        user = form.save()
        login(self.request, user)
        return response


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"


class LogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')
