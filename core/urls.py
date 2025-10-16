"""
Define las rutas URL para  "Salud Vital", estableciendo los endpoints para las operaciones CRUD
de las principales entidades del sistema: médicos, pacientes, especialidades, consultas médicas, tratamientos,
medicamentos, recetas médicas y detalles de recetas.

Utiliza una función auxiliar `generate_crud_urls` para simplificar y estandarizar la generación de URLs
para las vistas de lista, creación, actualización y eliminación, mejorando la mantenibilidad y claridad del código.

Incluye también la ruta principal que apunta a la vista base/index del sistema.
"""

from django.urls import path
from core.utils import generate_crud_urls
from core.views.medico import MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView
from core.views.paciente import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView
from core.views.especialidad import EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView
from core.views.consulta_medica import ConsultaMedicaListView, ConsultaMedicaCreateView, ConsultaMedicaUpdateView, ConsultaMedicaDeleteView
from core.views.tratamiento import TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView
from core.views.medicamento import MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView
from core.views.receta_medica import RecetaMedicaListView, RecetaMedicaCreateView, RecetaMedicaUpdateView, RecetaMedicaDeleteView
from core.views.detalle_receta import DetalleRecetaListView, DetalleRecetaCreateView, DetalleRecetaUpdateView, DetalleRecetaDeleteView
from .views import base

urlpatterns = [
    path('', base.index, name='index'),
]

urlpatterns += generate_crud_urls('medico', { 
    'list': MedicoListView.as_view(),
    'create': MedicoCreateView.as_view(),
    'update': MedicoUpdateView.as_view(),
    'delete': MedicoDeleteView.as_view(),
})

urlpatterns += generate_crud_urls('paciente', {
    'list': PacienteListView.as_view(),
    'create': PacienteCreateView.as_view(),
    'update': PacienteUpdateView.as_view(),
    'delete': PacienteDeleteView.as_view(),
})

urlpatterns += generate_crud_urls('consulta_medica', {
    'list': ConsultaMedicaListView.as_view(),
    'create': ConsultaMedicaCreateView.as_view(),
    'update': ConsultaMedicaUpdateView.as_view(),
    'delete': ConsultaMedicaDeleteView.as_view(),
})
urlpatterns += generate_crud_urls('detalle_receta', {
    'list': DetalleRecetaListView.as_view(),
    'create': DetalleRecetaCreateView.as_view(),
    'update': DetalleRecetaUpdateView.as_view(),
    'delete': DetalleRecetaDeleteView.as_view(),
})

urlpatterns += generate_crud_urls('especialidad', {
    'list': EspecialidadListView.as_view(),
    'create': EspecialidadCreateView.as_view(),
    'update': EspecialidadUpdateView.as_view(),
    'delete': EspecialidadDeleteView.as_view(),
})

urlpatterns += generate_crud_urls('receta_medica', {
    'list': RecetaMedicaListView.as_view(),
    'create': RecetaMedicaCreateView.as_view(),
    'update': RecetaMedicaUpdateView.as_view(),
    'delete': RecetaMedicaDeleteView.as_view(),
})

urlpatterns += generate_crud_urls('medicamento', {
    'list': MedicamentoListView.as_view(),
    'create': MedicamentoCreateView.as_view(),
    'update': MedicamentoUpdateView.as_view(),
    'delete': MedicamentoDeleteView.as_view(),
})

urlpatterns += generate_crud_urls('tratamiento', {
    'list': TratamientoListView.as_view(),
    'create': TratamientoCreateView.as_view(),
    'update': TratamientoUpdateView.as_view(),
    'delete': TratamientoDeleteView.as_view(),
})




