"""
Define filtros personalizados basados en django-filters para facilitar la búsqueda y
filtrado de datos en las vistas de la aplicación. Incluye un filtro base que adapta etiquetas
de búsqueda para mejorar la experiencia del usuario y filtros específicos para cada modelo,
permitiendo búsquedas por campos clave con soporte para rangos y coincidencias parciales.
"""

import django_filters
from .models import (
    Especialidad,
    Paciente,
    Medico,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
    DetalleReceta,
)

class BaseFilterSet(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, filter_obj in self.filters.items():
            if hasattr(filter_obj, 'lookup_expr') and filter_obj.lookup_expr == 'icontains':
                filter_obj.label = filter_obj.field_name.capitalize()

class EspecialidadFilter(BaseFilterSet):
    class Meta:
        model = Especialidad
        fields = {
            'nombre': ['icontains'],
        }

class PacienteFilter(BaseFilterSet):
    class Meta:
        model = Paciente
        fields = {
            'nombre': ['icontains'],
        }

class MedicoFilter(BaseFilterSet):
    class Meta:
        model = Medico
        fields = {
            'nombre': ['icontains'],
            'especialidad': ['exact'],
            'centro': ['exact'],
        }

class ConsultaMedicaFilter(BaseFilterSet):
    fecha = django_filters.DateFromToRangeFilter(label='Rango de fechas')

    class Meta:
        model = ConsultaMedica
        fields = {
            'fecha': ['exact'],
            'medico': ['exact'],
            'paciente': ['exact'],
            'estado': ['exact'],
        }

class TratamientoFilter(BaseFilterSet):
    class Meta:
        model = Tratamiento
        fields = {
            'descripcion': ['icontains'],
        }

class MedicamentoFilter(BaseFilterSet):
    class Meta:
        model = Medicamento
        fields = {
            'nombre': ['icontains'],
        }

class RecetaMedicaFilter(BaseFilterSet):
    class Meta:
        model = RecetaMedica
        fields = {
            'consulta': ['exact'],
            'fecha_emision': ['exact'],
        }

class DetalleRecetaFilter(BaseFilterSet):
    class Meta:
        model = DetalleReceta
        fields = {
            'receta': ['exact'],
            'medicamento': ['exact'],
        }