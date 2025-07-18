from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_confession, update_confession, delete_confession, home_page, logout_user, landing_page

app_name = "confession_app"

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('home/', home_page.as_view(), name="all"),
    path('home/create/', create_confession.as_view(), name="create_confession"),
    path('home/<int:pk>/update/', update_confession.as_view(), name="update_confession"),
    path('home/<int:pk>/delete/', delete_confession.as_view(), name="delete_confession"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="login.html"),name="login_page"),
    path("accounts/logout/", logout_user, name="logout")
]