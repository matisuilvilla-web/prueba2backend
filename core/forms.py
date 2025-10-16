"""
Módulo que define los formularios de Django para las entidades principales del sistema .
Cada formulario está basado en un ModelForm asociado a un modelo específico,
con widgets personalizados que incluyen placeholders y clases CSS para mejorar la experiencia de usuario.
Estos formularios facilitan la validación y presentación coherente de los datos en la interfaz web.
"""


from django import forms
from .models import (
    Especialidad,
    Paciente,
    Medico,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
    DetalleReceta,
)

class EspecialidadForm(forms.ModelForm):

    class Meta:
        model = Especialidad
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Cardiología',
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Ej: Especialidad médica enfocada en enfermedades del corazón.',
                'rows': 3,
                'class': 'form-control'
            }),
        }


class PacienteForm(forms.ModelForm):
   
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Juan Pérez',
                'class': 'form-control'
            }),
            'rut': forms.TextInput(attrs={
                'placeholder': 'Ej: 12.345.678-9',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ej: juan.perez@gmail.com',
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'placeholder': '+56 9 1234 5678',
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Ej: Av. Libertador 1234, Santiago',
                'class': 'form-control'
            }),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }


class MedicoForm(forms.ModelForm):
    
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Dra. Ana Rojas',
                'class': 'form-control'
            }),
            'matricula': forms.TextInput(attrs={
                'placeholder': 'Ej: M12345',
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'placeholder': '+56 9 8765 4321',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ej: ana.rojas@clinicacentral.cl',
                'class': 'form-control'
            }),
            'especialidad': forms.Select(attrs={'class': 'form-select'}),
            'centro': forms.Select(attrs={'class': 'form-select'}),
        }


class ConsultaMedicaForm(forms.ModelForm):
    
    class Meta:
        model = ConsultaMedica
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'fecha_consulta': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'motivo': forms.Textarea(attrs={
                'placeholder': 'Ej: Dolor torácico y dificultad para respirar.',
                'rows': 3,
                'class': 'form-control'
            }),
            'diagnostico': forms.Textarea(attrs={
                'placeholder': 'Ej: Posible angina de pecho.',
                'rows': 2,
                'class': 'form-control'
            }),
        }


class TratamientoForm(forms.ModelForm):
   
    class Meta:
        model = Tratamiento
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Rehabilitación cardíaca',
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Ej: Programa de ejercicios supervisados post infarto.',
                'rows': 3,
                'class': 'form-control'
            }),
            'duracion_dias': forms.NumberInput(attrs={
                'placeholder': 'Ej: 30',
                'class': 'form-control'
            }),
        }


class MedicamentoForm(forms.ModelForm):
    
    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Losartán 50mg',
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Ej: Antihipertensivo indicado para presión alta.',
                'rows': 2,
                'class': 'form-control'
            }),
            'fabricante': forms.TextInput(attrs={
                'placeholder': 'Ej: Laboratorio Chile',
                'class': 'form-control'
            }),
        }


class RecetaMedicaForm(forms.ModelForm):
    
    class Meta:
        model = RecetaMedica
        fields = '__all__'
        widgets = {
            'consulta': forms.Select(attrs={'class': 'form-select'}),
            'fecha_emision': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'indicaciones': forms.Textarea(attrs={
                'placeholder': 'Ej: Tomar 1 comprimido de Losartán cada 12 horas.',
                'rows': 3,
                'class': 'form-control'
            }),
        }
class DetalleRecetaForm(forms.ModelForm):
    
    class Meta:
        model = DetalleReceta
        fields = '__all__'
        widgets = {
            'receta': forms.Select(attrs={
                'class': 'form-control'
            }),
            'medicamento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dosis': forms.TextInput(attrs={
                'placeholder': 'Ej: 500 mg cada 8 horas',
                'class': 'form-control'
            }),
            'frecuencia': forms.TextInput(attrs={
                'placeholder': 'Ej: Cada 8 horas por 7 días',
                'class': 'form-control'
            }),
            'duracion_dias': forms.NumberInput(attrs={
                'placeholder': 'Ej: 7',
                'class': 'form-control'
            }),
        }