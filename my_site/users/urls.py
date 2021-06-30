from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",LoginView.as_view(template_name="users/login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("account/",views.account,name="account"),
    path("account/edit_user/",views.edit_user,name="edit_user"),
]