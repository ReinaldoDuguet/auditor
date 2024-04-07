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
    
    def post(self, request, format=None):
        data = request.data
        if data['nombre_empresa'] and data['nombre_contador']:
            
            nueva_empresa = Empresa(
                nombre_contador= data['nombre_contador'],
                nombre_empresa= data['nombre_empresa'],
                is_active= True,
                time_recorded= datetime.datetime.now()
            )
        nueva_empresa.save()
        return Response({"Empresa grabada en la bbdd":nueva_empresa.nombre_empresa})
    
    def delete(self, request, format=None):
        data = request.data
        
        if not data['nombre_empresa'] :
            return Rsponse('El nombre de la empresa no fue proporcionado')
        else:
            empresa_a_borrar = data['nombre_empresa']
            Empresa.objects.filter(nombre_empresa=empresa_a_borrar).delete()

            return Response({"Empresa removida existosamente":empresa_a_borrar})


class CuentaView(APIView):
    
    def get(self, request, format=None):
        data = request.data
        nombre_empresa = data.get('nombre_empresa', '')  
        empresa = Empresa.objects.filter(nombre_empresa=nombre_empresa).first()         
        
        if empresa:
            cuentas_padres = CuentaPadre.objects.filter(nombre_empresa=empresa)  
            diccionario_cuentas = {}

            for cuenta_padre in cuentas_padres:
                cuentas_hijas = CuentaHija.objects.filter(nombre_empresa=cuenta_padre)
                cuentas_hijas_info = {}

                for cuenta_hija in cuentas_hijas:
                    cuentas_hijas_info[cuenta_hija.nombre_cuenta] = {
                        "abono": cuenta_hija.abono,
                        "cargo": cuenta_hija.cargo
                    }

                diccionario_cuentas[cuenta_padre.nombre_cuenta] = cuentas_hijas_info

            return Response(diccionario_cuentas)
        else:
            return Response({"error": "No se encontró la empresa especificada"})

    
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
    

class CuentaPadreView(APIView):
    
    def post(self, request, format=None):
        data = request.data
        
        if not data['nombre_empresa']:
            return Response({"mensaje error":"falta nombre de la empresa"})
        
        elif data['nombre_empresa'] and data['nombre_cuenta'] is not None:
            nombre_empresa = data.get('nombre_empresa')
            nombre_cuenta = data.get('nombre_cuenta')
            
            empresa = Empresa.objects.filter(nombre_empresa=nombre_empresa).first()
            nueva_cuenta_padre = CuentaPadre(
                nombre_empresa=  empresa,
                nombre_cuenta= data['nombre_cuenta']
            )
            nueva_cuenta_padre.save()

        return Response({"Cuenta Padre guardada exitosamente": nombre_cuenta})
    
    def delete(self, request, format=None):
        data = request.data
        
        #falta agregar nombre de la empresa primero
        cuenta_a_borrar = CuentaPadre.objects.filter(nombre_cuenta=data['nombre_cuenta'])
        cuenta_a_borrar.delete()
        
        return Response({"cuenta borrada con exito":cuenta_a_borrar})