"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""

from core.models import DetalleReceta
from core.forms import DetalleRecetaForm 
from core.filters import DetalleRecetaFilter 
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class DetalleRecetaListView(BaseListView):
    model = DetalleReceta
    template_name = 'core/detalle_receta/list.html'
    context_object_name = 'detalle_recetas'  
    filterset_class = DetalleRecetaFilter

class DetalleRecetaCreateView(BaseCreateView):
    model = DetalleReceta
    form_class = DetalleRecetaForm
    template_name = 'core/detalle_receta/form.html'
    success_url = reverse_lazy('detalle_receta_list')

class DetalleRecetaUpdateView(BaseUpdateView):
    model = DetalleReceta
    form_class = DetalleRecetaForm
    template_name = 'core/detalle_receta/form.html'
    success_url = reverse_lazy('detalle_receta_list')

class DetalleRecetaDeleteView(BaseDeleteView):
    model = DetalleReceta
    template_name = 'core/detalle_receta/confirm_delete.html'
    success_url = reverse_lazy('detalle_receta_list')
