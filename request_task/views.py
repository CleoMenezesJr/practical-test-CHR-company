from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Jurisprudence
from .restapi import ResolveRequests


# Create your views here.
def search_jurisprudence(request: WSGIRequest) -> HttpResponse:
    return render(request, "list_jurisprudences.html")


def list_jurisprudences(request: WSGIRequest) -> HttpResponse:
    response = ResolveRequests(
        page=1, search=request.POST["search-input"]
    ).resolve_post()
    jurisprudences = Jurisprudence.objects.filter(id__in=response["jurisprudencias"])

    return render(
        request,
        "list_jurisprudences.html",
        {"jurisprudences": jurisprudences, "response": response},
    )
