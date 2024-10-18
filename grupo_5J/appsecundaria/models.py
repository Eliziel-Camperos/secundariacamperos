from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno = models.CharField(max_length=50, verbose_name='Apaterno')
    amaterno = models.CharField(max_length=50, verbose_name='Amaterno')
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    fecha_naci = models.DateField(verbose_name='Fecha de Nacimiento', null=False, blank=False)
    fecha_falle = models.DateField(verbose_name='Fallecimiento', null=True, blank=True)
    fecha_ingre = models.DateField(verbose_name='Ingreso', null=True, blank=True)
    
    class Meta:
        db_table = "Alumnos"
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self) -> str:
        return f"{self.apaterno} {self.amaterno}, {self.nombres}"


class Frase(models.Model):
    comentario = models.TextField(verbose_name='Comentario', max_length=400)
    Alumno_fk = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='frases')

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self) -> str:
        return self.comentario[:20]
