from rest_framework import serializers
from .models import *
from datetime import datetime


class EmpresaSerializer(serializers.ModelSerializer):
        class Meta:
            model   = Empresa
            fields  = '__all__'

class CuentaPadreSerializer(serializers.ModelSerializer):
        class Meta:
            model   = CuentaPadre
            fields  = '__all__'

class CuentaHijaSerializer(serializers.ModelSerializer):
        class Meta:
            model   = CuentaHija
            fields  = '__all__'

