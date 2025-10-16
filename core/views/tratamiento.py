"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import Tratamiento
from core.forms import TratamientoForm 
from core.filters import TratamientoFilter 
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class TratamientoListView(BaseListView):
    model = Tratamiento
    template_name = 'core/tratamiento/list.html'
    context_object_name = 'tratamientos'
    filterset_class = TratamientoFilter

class TratamientoCreateView(BaseCreateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'core/tratamiento/form.html'
    success_url = reverse_lazy('tratamiento_list')

class TratamientoUpdateView(BaseUpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'core/tratamiento/form.html'
    success_url = reverse_lazy('tratamiento_list')

class TratamientoDeleteView(BaseDeleteView):
    model = Tratamiento
    template_name = 'core/tratamiento/confirm_delete.html'
    success_url = reverse_lazy('tratamiento_list')
