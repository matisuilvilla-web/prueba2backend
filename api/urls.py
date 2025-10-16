from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadViewSet, MedicoViewSet, PacienteViewSet,
    ConsultaMedicaViewSet, TratamientoViewSet, MedicamentoViewSet,
    RecetaMedicaViewSet, DetalleRecetaViewSet
)

router = DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaMedicaViewSet)
router.register(r'detalles-receta', DetalleRecetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
