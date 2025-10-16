"""
Contiene los conjuntos de vistas (ViewSets) basados en ModelViewSet de Django REST Framework.
Estos manejan las operaciones CRUD para cada modelo del sistema a través de la API REST,
utilizando los serializadores correspondientes para la validación y la serialización de datos.
"""

from rest_framework import viewsets
from core.models import (
    Especialidad, Medico, Paciente, ConsultaMedica,
    Tratamiento, Medicamento, RecetaMedica, DetalleReceta
)
from .serializers import (
    EspecialidadSerializer, MedicoSerializer, PacienteSerializer,
    ConsultaMedicaSerializer, TratamientoSerializer,
    MedicamentoSerializer, RecetaMedicaSerializer, DetalleRecetaSerializer
)

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class DetalleRecetaViewSet(viewsets.ModelViewSet):
    queryset = DetalleReceta.objects.all()
    serializer_class = DetalleRecetaSerializer

class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
