from django.shortcuts import render
from .models import Alumno, Frase

# Create your views here.
def index_vista(request):
    alumnos = Alumno.objects.all().order_by('id')
    return render(request, "index.html", {"alumnos": alumnos})
