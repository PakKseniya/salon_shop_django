from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):

        """Аутентификация пользователя"""
        context = {}
        if request.method == 'POST':
            username = request.POST['username']

            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("user:profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
    template_name = "registration/profile.html"


class ProfileInfo(TemplateView):
    template_name = 'registration/profile_info.html'


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):

        """Регистрация пользователя"""

        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                         email=email, password=password)
                return redirect(reverse("user:login"))
        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = "registration/logged_out.html"

    def dispatch(self, request, *args, **kwargs):

        """Выход из личного кабинета"""

        logout(request)
        return render(request, self.template_name)

