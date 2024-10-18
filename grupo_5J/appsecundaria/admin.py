from django.contrib import admin
from .models import Alumno, Frase

class ComentarioIntLine(admin.TabularInline):
    model = Frase
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    fields = ['apaterno', 'amaterno', 'nombres', 'fecha_naci', 'fecha_ingre', 'fecha_falle']
    list_display = ['apaterno', 'amaterno', 'nombres', 'fecha_naci']
    
    inlines = [ComentarioIntLine]
    
admin.site.register(Alumno, AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields = ['comentario', 'alumno_fk']
    list_display = ['comentario']
