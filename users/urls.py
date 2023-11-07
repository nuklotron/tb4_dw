from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import DetailView, ConfirmPass, LoginUserView, login_view

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/login/', login_view, name='log'),

    path('main/', ConfirmPass.as_view(template_name='users/confirmpass.html'), name='confirm pass'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
]
