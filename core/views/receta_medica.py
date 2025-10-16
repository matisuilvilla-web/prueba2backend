"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import RecetaMedica
from core.forms import RecetaMedicaForm
from core.filters import RecetaMedicaFilter
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class RecetaMedicaListView(BaseListView):
    model = RecetaMedica
    template_name = 'core/receta_medica/list.html'
    context_object_name = 'recetas_medicas'  
    filterset_class = RecetaMedicaFilter

class RecetaMedicaCreateView(BaseCreateView):
    model = RecetaMedica
    form_class = RecetaMedicaForm
    template_name = 'core/receta_medica/form.html'
    success_url = reverse_lazy('receta_medica_list')

class RecetaMedicaUpdateView(BaseUpdateView):
    model = RecetaMedica
    form_class = RecetaMedicaForm 
    template_name = 'core/receta_medica/form.html'
    success_url = reverse_lazy('receta_medica_list')

class RecetaMedicaDeleteView(BaseDeleteView):
    model = RecetaMedica
    template_name = 'core/receta_medica/confirm_delete.html'
    success_url = reverse_lazy('receta_medica_list')

