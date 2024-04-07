from django.urls import path
from api import views

urlpatterns = [
    path('getEmpresas/', views.EmpresaView.as_view()),
    path('postEmpresas/', views.EmpresaView.as_view()),
    path('deleteEmpresas/', views.EmpresaView.as_view()),
    path('getCuentas/', views.CuentaView.as_view()),
    path('agregarCuentaPadre/', views.CuentaPadreView.as_view()),
    path('deleteCuentaPadre/', views.CuentaPadreView.as_view()),
]
