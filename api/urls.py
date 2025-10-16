from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadViewSet, MedicoViewSet, PacienteViewSet,
    ConsultaMedicaViewSet, TratamientoViewSet, MedicamentoViewSet,
    RecetaMedicaViewSet, DetalleRecetaViewSet
)

"""
Módulo de enrutamiento para los endpoints de la API REST del sistema Salud Vital.

Define las rutas para los recursos de la API, tales como médicos, pacientes,
consultas médicas, tratamientos, recetas y medicamentos.

Estas rutas devuelven datos en formato JSON y están orientadas al consumo
por clientes frontend o integraciones externas.
"""


router = DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaMedicaViewSet)
router.register(r'detalles-recetas', DetalleRecetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
