from django.contrib import admin
from .models import Empresa, CuentaHija, CuentaPadre
# Register your models here.


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa','nombre_contador')
    list_filter = ['nombre_contador']
    list_per_page = 10

    
@admin.register(CuentaHija)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cuenta','nombre_empresa','abono','cargo')
    list_filter = ['nombre_empresa']
    list_per_page = 10

@admin.register(CuentaPadre)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cuenta','nombre_empresa')
    list_filter = ['nombre_empresa']
    list_per_page = 10
#admin.site.register(Empresa)
#admin.site.register(Cuenta)