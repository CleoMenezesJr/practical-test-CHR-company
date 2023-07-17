from django.urls import path
from .views import show_json

urlpatterns = [
    path("", show_json, name="show_json"),
]
