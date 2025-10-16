"""
- Heredan de clases base reutilizables (`BaseListView`, `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`) que encapsulan 
  la funcionalidad común para listar, crear, actualizar y eliminar registros.  
- Cada vista especifica el modelo, el formulario asociado, la plantilla a usar y la URL de éxito para redirección.  
- La vista de listado incluye soporte para filtros mediante `filterset_class` para mejorar la experiencia de búsqueda y 
  filtrado de datos.  

Esta estructura modular y genérica facilita la extensión y mantenimiento del sistema, permitiendo replicar fácilmente el 
patrón para otros modelos simplemente cambiando los parámetros específicos.
"""


from core.models import ConsultaMedica
from core.forms import ConsultaMedicaForm
from core.filters import ConsultaMedicaFilter
from django.urls import reverse_lazy
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

class ConsultaMedicaListView(BaseListView):
    model = ConsultaMedica
    template_name = 'core/consulta_medica/list.html'
    context_object_name = 'consultas_medicas'
    filterset_class = ConsultaMedicaFilter

class ConsultaMedicaCreateView(BaseCreateView):
    model = ConsultaMedica
    form_class = ConsultaMedicaForm
    template_name = 'core/consulta_medica/form.html'
    success_url = reverse_lazy('consulta_medica_list')

class ConsultaMedicaUpdateView(BaseUpdateView):
    model = ConsultaMedica
    form_class = ConsultaMedicaForm
    template_name = 'core/consulta_medica/form.html'
    success_url = reverse_lazy('consulta_medica_list')

class ConsultaMedicaDeleteView(BaseDeleteView):
    model = ConsultaMedica
    template_name = 'core/consulta_medica/confirm_delete.html'
    success_url = reverse_lazy('consulta_medica_list')
