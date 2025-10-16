"""
Define los modelos principales de "Salud Vital", representando las entidades del sistema de salud.
Incluye especialidades médicas, centros médicos, médicos, pacientes, consultas médicas, tratamientos, medicamentos,
recetas médicas y detalles de recetas. Cada modelo contiene campos relevantes y relaciones entre entidades,
permitiendo la gestión estructurada y coherente de la información clínica.
"""

from django.db import models


class Especialidad(models.Model):
  
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class CentroMedico(models.Model):
  
    nombre = models.CharField(max_length=150, unique=True)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
   
    nombre = models.CharField(max_length=120)
    matricula = models.CharField(max_length=50, unique=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name='medicos')
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    centro = models.ForeignKey(CentroMedico, on_delete=models.CASCADE, related_name='medicos')


    def __str__(self):
        return f"{self.nombre} ({self.matricula})"
    

class Paciente(models.Model):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    nombre = models.CharField(max_length=120)
    rut = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.rut}"


class ConsultaMedica(models.Model):
 
    ESTADO_CHOICES = [
        ('PEND', 'Pendiente'),
        ('REAL', 'Realizada'),
        ('CANC', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, related_name='consultas')
    fecha = models.DateTimeField()
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=5, choices=ESTADO_CHOICES, default='PEND')

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente.nombre} ({self.fecha.date()})"


class Tratamiento(models.Model):
   
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE, related_name='tratamientos')
    descripcion = models.TextField()
    duracion_dias = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Tratamiento {self.id} - Consulta {self.consulta.id}"


class Medicamento(models.Model):
  
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    dosis_recomendada = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class RecetaMedica(models.Model):
 
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE, related_name='recetas')
    fecha_emision = models.DateField(auto_now_add=True)
    medicamentos = models.ManyToManyField(Medicamento, through='DetalleReceta')

    def __str__(self):
        return f"Receta {self.id} - Consulta {self.consulta.id}"


class DetalleReceta(models.Model):

    receta = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.medicamento.nombre} - {self.receta.id}"
