"""
Contiene las vistas base y genéricas  "Salud Vital". 

- `index`: Vista simple que renderiza la página principal del sistema.
- `BaseListView`: Vista genérica para listar objetos con soporte opcional para filtros usando django-filters.
  Maneja la obtención del queryset filtrado y pasa el filtro al contexto para facilitar la integración en las plantillas.
- `BaseCreateView`, `BaseUpdateView`, `BaseDeleteView`: Vistas genéricas base para crear, actualizar y eliminar
  registros respectivamente. Se definen con atributos para la plantilla y la URL de redirección luego de la acción.
  
Estas clases base están pensadas para ser heredadas por vistas específicas de cada modelo, promoviendo la reutilización
y estandarización del código.
"""

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django_filters.views import FilterView

def index(request):
    return render(request, 'core/index.html')

class BaseListView(ListView):
    template_name = ''
    context_object_name = ''
    filterset_class = None 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.filterset_class:
            self.filter = self.filterset_class(self.request.GET, queryset=queryset)
            return self.filter.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'filter'):
            context['filter'] = self.filter
        return context

class BaseCreateView(CreateView):
    template_name = ''
    success_url = ''
   

class BaseUpdateView(UpdateView):
    template_name = ''
    success_url = ''
   

class BaseDeleteView(DeleteView):
    template_name = ''
    success_url = ''
