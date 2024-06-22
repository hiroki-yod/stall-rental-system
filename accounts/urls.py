from django.urls import path
from .views import IndexView, SignUpView, LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
