from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    nombre = 'Adrian'
    apellido = 'Castillo'
    fecha = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')

    lista = ['Diccionarios', 'Modulos', 'Metodos', 'Atributos', 'Plantillas']        

    doc_externo = open('C:/Users/Adrian12/Desktop/Curso_Django/Proyecto1/Proyecto1/plantillas/plantilla1.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({'nombre_p': nombre, 'apellido_p': apellido, 'hora_fecha':fecha, 'items':lista})
    documento= plt.render(ctx)

    return HttpResponse(documento)


def fecha(request):

    tiempo = datetime.datetime.now()

    return HttpResponse("""

    <html>
    <body>
    <h1> 
    fecha y hora %s
    </h1>
    </body>
    </html>

""" %tiempo)


def edad(request, ano, edad):

    


    edad_futura = ano-2023
    edad_futura = edad_futura + edad

    return HttpResponse(edad)


