from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html = "<html><body>Harrys eres genial</body></html>"
    return HttpResponse(html)


from django.template import loader
def index(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())


def empleados(request):
   template = loader.get_template('empleados.html')
   return HttpResponse(template.render())   
def clientes(request):
   template = loader.get_template('clientes.html')
   return HttpResponse(template.render())      
def productos(request):
   template = loader.get_template('productos.html')
   return HttpResponse(template.render()) 

def regiones(request):
   template = loader.get_template('regiones.html')
   return HttpResponse(template.render())              