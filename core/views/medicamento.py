"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import Medicamento
from core.forms import MedicamentoForm
from core.filters import MedicamentoFilter
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class MedicamentoListView(BaseListView):
    model = Medicamento
    template_name = 'core/medicamento/list.html'
    context_object_name = 'medicamentos'
    filterset_class = MedicamentoFilter 

class MedicamentoCreateView(BaseCreateView):
    model = Medicamento
    form_class = MedicamentoForm 
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('medicamento_list')

class MedicamentoUpdateView(BaseUpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('medicamento_list')

class MedicamentoDeleteView(BaseDeleteView):
    model = Medicamento
    template_name = 'core/medicamento/confirm_delete.html'
    success_url = reverse_lazy('medicamento_list')
