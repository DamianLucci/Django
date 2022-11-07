from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def vista_saludo(request):
    return HttpResponse("Hola coders")

def iniciar_sesion(request):
    return HttpResponse("pasame tu username")

def dia_hoy(request, nombre):
    hoy = datetime.now()
    
    respuesta = f"hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)
    
def anio_nacimiento(request, edad):
    edad = int(edad)
    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac}")
 
 
def vista_plantillahtml(request):
    archivo = open(r"C:\Users\ADMIN\Desktop\Django\codigo\proyectocoder\templates\plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context()

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def vista_familiares(request):
    archivo = open(r"C:\Users\ADMIN\Desktop\Django\codigo\proyectocoder\templates\familiares.html")

    plantilla = Template(archivo.read())

    archivo.close()
    listado_familiares= ["F1","F2"]
    
    datos = {"listado_familiares":listado_familiares }

    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)