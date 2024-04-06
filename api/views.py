from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import ipdb
import datetime

from . import serializers
from .models import *
# Create your views here.

class EmpresaView(APIView):
    
    def get(self, request, format=None):
        data = request.data
        contador = data['nombre_contador']
        empresas = Empresa.objects.filter(nombre_contador=contador)
        nombre_empresas = list(empresas.values_list('nombre_empresa', flat=True))
        
        return Response({'empresas':nombre_empresas})


class CuentaView(APIView):
    
    def get(self, request, format=None):
        data = request.data
        nombre_empresa = data['nombre_empresa']
        empresa_id = Empresa.objects.get(nombre_empresa=nombre_empresa).id
        cuentas_padres = CuentaPadre.objects.filter(nombre_empresa=empresa_id).values()
        cuentas_hijas = CuentaHija.objects.filter(nombre_empresa=empresa_id).values()

        #ipdb.set_trace()
        cuentas_listado_hijas =  list(cuentas_hijas.values_list("nombre_cuenta",flat=True))
        cuentas_listado_padres =  list(cuentas_padres.values_list("nombre_cuenta",flat=True))
        cuentas_listado_abono =  list(cuentas_hijas.values_list("abono",flat=True))
        cuentas_listado_cargo =  list(cuentas_hijas.values_list("cargo",flat=True))
        
        print(f'las cuentas son: {cuentas_listado_hijas}\n')
        print(f'las cuentas padres son: {cuentas_listado_padres}\n')
        print(f'la cuenta ABONO es: {cuentas_listado_abono}\n')
        print(f'la cuenta CARGO es: {cuentas_listado_cargo}\n')
        
        diccionario_cuentas_padres = {}
        diccionario_cuentas_hijas = {}
        
        for cuenta_padre in cuentas_listado_padres:
            diccionario_cuentas_padres[cuenta_padre] = {}

            for cuenta_hija, abono, cargo in zip(cuentas_listado_hijas, cuentas_listado_abono, cuentas_listado_cargo):
                diccionario_cuentas_padres[cuenta_padre][cuenta_hija] = {
                    "abono" : abono,
                    "cargo" : cargo
                }
            #    diccionario_cuentas_hijas[cuenta_hija] = {
            #        "abono":abono,
            #        "cargo":cargo
            #    }
   
        return Response(diccionario_cuentas_padres)
    
    def put(self, request, format=None):
        data = request.data
        nombre_empresa = data['nombre_empresa']
        nombre_cuenta  = data['nombre_cuenta']
        
        #tener en cuenta que es cargo o abono
        cargo = 0
        abono = 0
        cargo = data['cargo']
        #abono = data['abono']
        
        empresa_id = Empresa.objects.get(nombre_empresa=nombre_empresa).id
        cuentas = Cuenta.objects.filter(nombre_empresa=empresa_id)
        cuentas_listado =  list(cuentas.values_list("nombre_cuenta",flat=True))
        
        if nombre_cuenta in cuentas_listado:
            print(f"la cuenta {nombre_cuenta} se enucentra en el listado a actualizar")
            
        else:
            print('no hay ná que modificar')
        
        return Response({'valores_actualizar':data})