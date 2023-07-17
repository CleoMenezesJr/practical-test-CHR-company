from requests import Session

from .models import Jurisprudence


class ResolveRequests:
    def __init__(self, page: int, search: str):
        with Session() as session:
            self.session = session

        self.url = "https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list"
        self.body = {
            "page": page,
            "pageSize": 10,
            "search": search,
            "orden": "nuevo",
        }

    def resolve_post(self) -> list:
        response = self.session.post(
            self.url,
            json=self.body,
        )

        return self.insert_jurisprudence_to_db(response.json())

    def insert_jurisprudence_to_db(self, jurisprudences: dict) -> dict:
        for jurisprudence in jurisprudences["jurisprudencias"]:
            juri = Jurisprudence(
                id=jurisprudence["id"],
                tipo_causa=jurisprudence["tipoCausa"],
                rol=jurisprudence["rol"],
                caratula=jurisprudence["caratula"],
                nombre_proyecto=jurisprudence["nombreProyecto"],
                fecha_sentencia=jurisprudence["fechaSentencia"],
                descriptores=jurisprudence["descriptores"],
                link_sentencia=jurisprudence["linkSentencia"],
                url_sentencia=jurisprudence["urlSentencia"],
                activo=jurisprudence["activo"],
                tribunal=jurisprudence["tribunal"],
                tipo=jurisprudence["tipo"],
                relacionada=jurisprudence["relacionada"],
                visitas=jurisprudence["visitas"],
            )
            juri.save()

        jurisprudences["jurisprudencias"] = [
            i["id"] for i in jurisprudences["jurisprudencias"]
        ]
        return jurisprudences
