from hello import views  # noqa: I001
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
]
