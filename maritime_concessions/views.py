import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import Concession
from .scraping import scrap_page


# Create your views here.
def show_json(request: WSGIRequest) -> HttpResponse:
    scrap_data = scrap_page()

    with open("concession.json", "w") as file:
        json.dump(scrap_data, file, indent=2)

    for data in scrap_data:
        concession = Concession(
            number=data["numero"],
            concession_number=data["numero_concecion"],
            concession_type=data["tipo_concesion"],
            commune=data["comuna"],
            location=data["lugar"],
            rs_ds=data["rs_ds"],
            tramite_type=data["tipo_tramite"],
            concessionaire=data["concesionario"],
            vigency_type=data["tipo_vigencia"],
        )
        concession.save()

    return render(request, "index.html", {"concessions": scrap_data})
