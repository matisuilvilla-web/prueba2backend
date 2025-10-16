from django.core.management.base import BaseCommand
from core.models import (
    Especialidad, CentroMedico, Medico, Paciente,
    ConsultaMedica, Tratamiento, Medicamento,
    RecetaMedica, DetalleReceta
)
from datetime import datetime, timedelta, date

class Command(BaseCommand):
    help = 'Carga datos iniciales'
    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando carga de datos...")

        # Crear especialidad
        cardio, _ = Especialidad.objects.get_or_create(
            nombre="Cardiología",
            descripcion="Especialidad médica que se ocupa del tratamiento del corazón y el sistema circulatorio."
        )

        # Crear centro médico
        clinica, _ = CentroMedico.objects.get_or_create(
            nombre="Clínica Central",
            direccion="Av. Salud 123, Santiago",
            telefono="229999999",
            ciudad="Santiago"
        )

        # Crear médico
        medico, _ = Medico.objects.get_or_create(
            nombre="Dr. Juan Pérez",
            matricula="M12345",
            especialidad=cardio,
            centro=clinica,
            telefono="912345678",
            email="juan.perez@clinicacentral.cl"
        )

        # Crear paciente
        paciente, _ = Paciente.objects.get_or_create(
            nombre="Ana López",
            rut="12.345.678-9",
            fecha_nacimiento=date(1990, 6, 12),
            sexo="F",
            telefono="987654321",
            direccion="Calle Falsa 123"
        )

        # Crear consulta médica
        consulta, _ = ConsultaMedica.objects.get_or_create(
            paciente=paciente,
            medico=medico,
            fecha=datetime.now(),
            motivo="Dolor en el pecho y dificultad para respirar.",
            diagnostico="Posible angina de pecho",
            estado="REAL"
        )

        # Crear tratamiento
        Tratamiento.objects.get_or_create(
            consulta=consulta,
            descripcion="Reposo, dieta baja en grasas, y evitar el estrés.",
            duracion_dias=14
        )

        # Crear medicamentos
        aspirin, _ = Medicamento.objects.get_or_create(
            nombre="Aspirina 100mg",
            descripcion="Antiinflamatorio y anticoagulante",
            dosis_recomendada="1 comprimido cada 12 horas"
        )

        enalapril, _ = Medicamento.objects.get_or_create(
            nombre="Enalapril 10mg",
            descripcion="Inhibidor de la ECA, usado para tratar la hipertensión",
            dosis_recomendada="1 comprimido al día"
        )

        # Crear receta médica
        receta, _ = RecetaMedica.objects.get_or_create(
            consulta=consulta
        )

        # Agregar medicamentos a la receta con detalle
        DetalleReceta.objects.get_or_create(
            receta=receta,
            medicamento=aspirin,
            dosis="100mg",
            frecuencia="Cada 12 horas"
        )

        DetalleReceta.objects.get_or_create(
            receta=receta,
            medicamento=enalapril,
            dosis="10mg",
            frecuencia="Cada 24 horas"
        )

        self.stdout.write(self.style.SUCCESS("Datos iniciales cargados correctamente."))
