from django.urls import path
from api import views

urlpatterns = [
    path('getEmpresas/', views.EmpresaView.as_view()),
    path('getCuentas/', views.CuentaView.as_view()),
]
