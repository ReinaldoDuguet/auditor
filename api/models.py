from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre_contador = models.CharField(max_length=100)
    nombre_empresa  = models.CharField(max_length=100)
    is_active       = models.BooleanField(default=True)
    time_recorded   = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre_empresa 
    

class CuentaPadre(models.Model):
    nombre_cuenta = models.CharField(max_length=50,)
    nombre_empresa= models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.nombre_cuenta} - {self.nombre_empresa}"

    
class CuentaHija(models.Model):
    nombre_cuenta = models.CharField(max_length=50,)
    cargo         = models.FloatField(default=0,null=True)
    abono         = models.FloatField(default=0, null= True)
    nombre_empresa= models.ForeignKey(CuentaPadre, on_delete=models.CASCADE)
    
    def __str__(self):
        return f" {self.nombre_cuenta} - {self.nombre_empresa}"
    
    
