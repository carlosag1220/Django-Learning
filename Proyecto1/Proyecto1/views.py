from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    p1 = Persona("Carlos Andres", "Aguirre")
    ahora = datetime.datetime.now()
    temas_curso = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]

    # Método 1: Leyendo la plantilla y creando un contexto
    # doc_externo = open("D:/Desktop/django-learning/Proyecto1/Proyecto1/plantillas/plantilla1.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    # ctx = Context(
    #     {
    #         "nombre_persona": p1.nombre,
    #         "apellido_persona": p1.apellido,
    #         "momento_actual": ahora,
    #         "temas": temas_curso,
    #     }
    # )
    # documento = plt.render(ctx)
    # return HttpResponse(documento)

    # Método 2: Cargando un diccionario al Loader
    # (Previamente se debió haber cargado la ruta de las plantillas en el archivo urls.py)
    # doc_externo = get_template("plantilla1.html")
    # documento = doc_externo.render(
    #     {
    #         "nombre_persona": p1.nombre,
    #         "apellido_persona": p1.apellido,
    #         "momento_actual": ahora,
    #         "temas": temas_curso,
    #     }
    # )
    # return HttpResponse(documento)

    # Método 2: Con Shortcuts
    return render(
        request,
        "plantilla1.html",
        {
            "nombre_persona": p1.nombre,
            "apellido_persona": p1.apellido,
            "momento_actual": ahora,
            "temas": temas_curso,
        },
    )


def cursoC(request):
    ahora = datetime.datetime.now()
    return render(request, "cursoC.html", {"momento_actual": ahora,})


def cursoCss(request):
    ahora = datetime.datetime.now()
    return render(request, "cursoCss.html", {"momento_actual": ahora,})


def despedida(request):
    return HttpResponse("Bye world")


def fecha_hora_actual(request):
    fecha = datetime.datetime.now()
    documento = (
        """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>"""
        % fecha
    )
    return HttpResponse(documento)


def calculaedad(request, edad, agno):
    periodo = agno - 2019
    edadfutura = edad + periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s
    </h2>
    </body>
    </html>""" % (
        agno,
        edadfutura,
    )
    return HttpResponse(documento)
