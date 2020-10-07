from django.http import HttpResponse
import datetime
from django.template import Template, Context

def welcome(request): # primera vista
    #--------------------codigo html
    document="""
    <html>
    <body>
    <h1  style="color:#FF0000";>
    My first response http
    </h1>
    </body>
    </html>"""
    return HttpResponse(document)

def todayTime(request):
    time_now=datetime.datetime.now()
    #--------------------codigo html
    document="""
    <html>
    <body>
    <h1  style="color:#FF0000";>
    My hours now is %s
    </h1>
    </body>
    </html>""" % time_now
    return HttpResponse(document)

def ageCalculate(request, year):
    ageCurrent=33
    period=year-2020
    ageFuture=ageCurrent+period
    document="""
    <html>
    <body>
    <h2>In the years %s you will be %s years old<h2>
    </html>
    </body>     
    """ %(year,ageFuture)
    return HttpResponse(document)

def new_template(request):
    doc_externo=open("C:/Users/JORGECC/Documents/CURSOS/DJANGO/proyecto1/proyecto1/plantilla/mytemplate.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    clx=Context()
    document=plt.render(clx)
    return HttpResponse(document)

