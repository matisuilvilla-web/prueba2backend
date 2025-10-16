"""
Define las rutas URL para "Salud Vital", estableciendo los endpoints para las operaciones CRUD
de las principales entidades del sistema: médicos, pacientes, especialidades, consultas médicas, tratamientos,
medicamentos, recetas médicas y detalles de recetas.

Utiliza la función auxiliar `generate_crud_urls` para estandarizar la generación de URLs
para las vistas de lista, creación, actualización y eliminación, mejorando la mantenibilidad.

Incluye también la ruta principal que apunta a la vista base/index del sistema.
"""
# Para agregar nuevas rutas CRUD:
# 1. Importar las 4 vistas: ListView, CreateView, UpdateView, DeleteView
# 2. Agregar una tupla en `crud_views` con el nombre y las vistas

from django.urls import path
from core.utils import generate_crud_urls
from .views import base

# Importar todas las vistas CRUD de los módulos correspondientes
from core.views.medico import MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView
from core.views.paciente import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView
from core.views.especialidad import EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView
from core.views.consulta_medica import ConsultaMedicaListView, ConsultaMedicaCreateView, ConsultaMedicaUpdateView, ConsultaMedicaDeleteView
from core.views.tratamiento import TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView
from core.views.medicamento import MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView
from core.views.receta_medica import RecetaMedicaListView, RecetaMedicaCreateView, RecetaMedicaUpdateView, RecetaMedicaDeleteView
from core.views.detalle_receta import DetalleRecetaListView, DetalleRecetaCreateView, DetalleRecetaUpdateView, DetalleRecetaDeleteView

urlpatterns = [
    path('', base.index, name='index'),
]

# Lista de entidades y sus vistas CRUD asociadas
crud_views = [
    ("medico", MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView),
    ("paciente", PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView),
    ("especialidad", EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView),
    ("consulta_medica", ConsultaMedicaListView, ConsultaMedicaCreateView, ConsultaMedicaUpdateView, ConsultaMedicaDeleteView),
    ("tratamiento", TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView),
    ("medicamento", MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView),
    ("receta_medica", RecetaMedicaListView, RecetaMedicaCreateView, RecetaMedicaUpdateView, RecetaMedicaDeleteView),
    ("detalle_receta", DetalleRecetaListView, DetalleRecetaCreateView, DetalleRecetaUpdateView, DetalleRecetaDeleteView),
]

# Generar automáticamente las URLs CRUD para cada entidad
for prefix, list_view, create_view, update_view, delete_view in crud_views:
    urlpatterns += generate_crud_urls(prefix, {
        'list': list_view.as_view(),
        'create': create_view.as_view(),
        'update': update_view.as_view(),
        'delete': delete_view.as_view(),
    })




