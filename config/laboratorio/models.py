from django.db import models

def validate_fecha_fabricacion(value):
    if value.year < 2015:
        raise ValidationError('La fecha de fabricación debe ser a partir de 2015.')
class Laboratorio(models.Model):
    nombre = models.CharField (max_length=100)
    ciudad = models.CharField(max_length=100, default='Null')  # Nueva migración
    pais = models.CharField(max_length=100, default='Null')  # Nuevo migración

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio,on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default='Null')

    class Meta:
        verbose_name_plural = "Directores Generales"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[validate_fecha_fabricacion])
    p_costo= models.DecimalField(max_digits=10, decimal_places=2)
    p_venta= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

