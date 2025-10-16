"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import Medico
from core.forms import MedicoForm
from core.filters import MedicoFilter
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class MedicoListView(BaseListView):
    model = Medico
    template_name = 'core/medico/list.html'
    context_object_name = 'medicos'
    filterset_class = MedicoFilter 

class MedicoCreateView(BaseCreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'core/medico/form.html'
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(BaseUpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'core/medico/form.html'
    success_url = reverse_lazy('medico_list')

class MedicoDeleteView(BaseDeleteView):
    model = Medico
    template_name = 'core/medico/confirm_delete.html'
    success_url = reverse_lazy('medico_list')
