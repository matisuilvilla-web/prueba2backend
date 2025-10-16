"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import Paciente
from core.forms import PacienteForm
from core.filters import PacienteFilter
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class PacienteListView(BaseListView):
    model = Paciente
    template_name = 'core/paciente/list.html'
    context_object_name = 'pacientes'
    filterset_class = PacienteFilter

class PacienteCreateView(BaseCreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(BaseUpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(BaseDeleteView):
    model = Paciente
    template_name = 'core/paciente/confirm_delete.html'
    success_url = reverse_lazy('paciente_list')
