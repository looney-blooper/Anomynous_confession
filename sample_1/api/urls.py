from django.urls import path
from .views import create_confession, update_confession, delete_confession, home_page

app_name = "api"
urlpatterns = [
    path('home/', home_page.as_view(), name="home_page"),
    path('home/create/', create_confession.as_view(), name="create_confession"),
    path('home/<int:pk>/update/', update_confession.as_view(), name="update_confession"),
    path('home/<int:pk>/delete/', delete_confession.as_view(), name="delete_confession"),
]