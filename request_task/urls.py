from django.urls import path
from .views import search_jurisprudence, list_jurisprudences

urlpatterns = [
    path("", search_jurisprudence),
    path("list/", list_jurisprudences, name="list_jurisp"),
]
