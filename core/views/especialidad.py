"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import Especialidad
from core.forms import EspecialidadForm 
from core.filters import EspecialidadFilter
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class EspecialidadListView(BaseListView):
    model = Especialidad
    template_name = 'core/especialidad/list.html'
    context_object_name = 'especialidades'
    filterset_class = EspecialidadFilter

class EspecialidadCreateView(BaseCreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'core/especialidad/form.html'
    success_url = reverse_lazy('especialidad_list')

class EspecialidadUpdateView(BaseUpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'core/especialidad/form.html'
    success_url = reverse_lazy('especialidad_list')

class EspecialidadDeleteView(BaseDeleteView):
    model = Especialidad
    template_name = 'core/especialidad/confirm_delete.html'
    success_url = reverse_lazy('especialidad_list')
