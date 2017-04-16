from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.core.mail import send_mail #Falta configurar los settings
import json

def index(request):
    return render(request, 'sitioWeb/index.html', {})


def correo_electronico(request):
    if request.method == 'POST':
        response_data = {}
        try:
            correo_cliente = request.POST.get('correo_electronico')
            nombre_cliente = request.POST.get('nombre')
            servicios_cliente = request.POST.get('contenido') #llamar por el nombre del objeto json que se envia como 'data' dentro de la consulta Ajax
            from_email=settings.EMAIL_HOST_USER
            to_list=[from_email]
            send_mail('Contacto de cliente desde el sitio','De: '+nombre_cliente+' <'+correo_cliente+'>'+'\n\n' +'\n\n' +servicios_cliente,from_email,to_list,fail_silently=False)
            response_data['Respuesta']='Gracias por tomarnos en cuenta.'+'\n\n'+'Pronto uno de nuestros miembros se pondra en contacto usted.'
        except Exception as e:
            response_data['Respuesta']='Ocurrió un error, por favor intente contactarnos de nuevo.'+'\n'+str(e)
        return HttpResponse(
            json.dumps(response_data,cls=DjangoJSONEncoder),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )