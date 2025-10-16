"""
Define los serializadores de Django REST Framework para las entidades principales del sistema.
Cada serializador transforma instancias de modelos en representaciones JSON y viceversa,
permitiendo la interacción a través de la API. Incluye campos relacionados como lecturas solo
y anidamientos para estructuras más complejas.
"""

from rest_framework import serializers
from core.models import (
    Especialidad, Medico, Paciente, ConsultaMedica,
    Tratamiento, Medicamento, RecetaMedica, DetalleReceta
)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    especialidad_nombre = serializers.ReadOnlyField(source='especialidad.nombre')

    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.ReadOnlyField(source='paciente.nombre')
    medico_nombre = serializers.ReadOnlyField(source='medico.nombre')

    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class DetalleRecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReceta
        fields = '__all__'

class RecetaMedicaSerializer(serializers.ModelSerializer):
    detalles = DetalleRecetaSerializer(source='detallereceta_set', many=True, read_only=True)

    class Meta:
        model = RecetaMedica
        fields = '__all__'

