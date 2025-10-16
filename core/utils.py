"""
Genera las rutas CRUD para el modelo correspondiente.
    
:param prefix: str - nombre base para la ruta y los nombres de URL (ej: 'medico')
:param views_dict: dict - diccionario con claves 'list', 'create', 'update', 'delete' y sus vistas
"""

from django.urls import path

def generate_crud_urls(prefix: str, views_dict: dict):

    return [
        path(f'{prefix}/', views_dict['list'], name=f'{prefix}_list'),
        path(f'{prefix}/nuevo/', views_dict['create'], name=f'{prefix}_create'),
        path(f'{prefix}/editar/<int:pk>/', views_dict['update'], name=f'{prefix}_update'),
        path(f'{prefix}/borrar/<int:pk>/', views_dict['delete'], name=f'{prefix}_delete'),
    ]


