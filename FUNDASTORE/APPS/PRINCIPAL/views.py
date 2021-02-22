from django.shortcuts import render
from django.core.mail import send_mail
from .forms import *


# Create your views here.
def ver_contactenos(request):
    formulario = FormularioContactenos()
    if request.method == "POST":
        formulario = FormularioContactenos(request.POST)
        asunto = 'CONSULTA DE -' + str(formulario["nombre"].value())
        mensaje = 'INFORMACION DE CONTACTO\nNOMBRE: [NOM]\nEMAIL: [EMAIL]\nTELEFONO: [TEL]\n\nMENSAJE\n[MSJ]'
        mensaje =mensaje.replace("[NOM]",formulario["nombre"].value())
        mensaje =mensaje.replace("[EMAIL]",formulario["email"].value())
        mensaje =mensaje.replace("[TEL]",formulario["telefono"].value())
        mensaje =mensaje.replace("[MSJ]",formulario["mensaje"].value())
        destinatarios = ["celsoarauz18@gmail.com"]
        send_mail(asunto,mensaje,None,destinatarios,fail_silently=False)
        asunto = 'SU CONSULTA HA SIDO RECIBIDA'
        mensaje = 'HEMOS RECIBIDO SU CONSULTA EN 3 DIAS TENDRA RESPUESTA'
        destinatarios = [str(formulario["email"].value())]
        send_mail(asunto,mensaje,None,destinatarios,fail_silently=False)
    else:
        formulario = FormularioContactenos()
    contexto = {"formulario":formulario}
    return render(request,'PRINCIPAL/contactenos.html',contexto)