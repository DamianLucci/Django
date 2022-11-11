from django.http import HttpResponse
from appcoder.models import Familia
from django.template import Template, Context, loader
# Create your views here.


def listado_familiares(request):
    
    familiares=Familia.objects.all()
    cadena_respuesta=""
    for familiar in familiares:
        cadena_respuesta+=familiar.nombre +" "+ familiar.apellido +" "+ familiar.fecha_nac + "-"
    

    return HttpResponse(cadena_respuesta)

 
def vista_plantillafamiliares(request):
    archivo = open(r"C:\Users\ADMIN\Desktop\Django\codigo\appcoder\templates\familiares.html")

    plantilla = Template(archivo.read()) #devuelve en un solo string todo el contenido del archivo html
    
    archivo.close()
    
    listado_familiares=Familia.objects.all()
    
    datos= {"listado_familiares": listado_familiares}
    
    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)