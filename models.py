from django.db import models

# Enumerations
class Estado(models.TextChoices):
    COMIENDO = 'COMIENDO'
    DORMIDO = 'DORMIDO'
    ENFERMO = 'ENFERMO'
    ESTRESADO = 'ESTRESADO'
    HAMBRIENTO = 'HAMBRIENTO'
    HERIDO = 'HERIDO'
    NORMAL = 'NORMAL'

class TipoDieta(models.TextChoices):
    CARNIVORO = 'CARNIVORO'
    HERVIVORO = 'HERVIVORO'
    OMNIVORO = 'OMNIVORO'

class TipoCuerpo(models.TextChoices):
    INVERTEBRADO = 'INVERTEBRADO'
    VERTEBRADO = 'VERTEBRADO'

class Zona(models.TextChoices):
    ESTE = 'ESTE'
    NORTE = 'NORTE'
    OESTE = 'OESTE'
    SUR = 'SUR'

class TipoAlimento(models.TextChoices):
    CARNE = 'CARNE'
    PESCADO = 'PESCADO'
    HIERBA = 'HIERBA'
    FRUTA = 'FRUTA'

# Models
class Direccion(models.Model):
    calle_principal = models.CharField(max_length=255)
    calle_secundaria = models.CharField(max_length=255)
    referencia = models.TextField()

    def mostrar_ubicacion(self):
        return f"{self.calle_principal} y {self.calle_secundaria} ({self.referencia})"

class Zoologico(models.Model):
    capacidad = models.IntegerField()
    nombre = models.CharField(max_length=255, null=False, blank=False)
    telefono = models.CharField(max_length=20)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def agregar_animal(self):
        pass

    def calcular_animales(self):
        return self.animal_set.count()

    def calcular_empleados(self):
        return self.empleado_set.count()

    def indicar_informacion(self):
        return f"{self.nombre}, Tel: {self.telefono}"

class SerVivo(models.Model):
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=255)

    def calcular_edad(self):
        from datetime import date
        return date.today().year - self.fecha_nacimiento.year

class Animal(SerVivo):
    contador = models.IntegerField()
    edad = models.IntegerField()
    nombre_cientifico = models.CharField(max_length=255)
    peso = models.FloatField()
    tipo_dieta = models.CharField(max_length=10, choices=TipoDieta.choices, null=True)
    tipo_cuerpo = models.CharField(max_length=12, choices=TipoCuerpo.choices, null=True)
    estado = models.CharField(max_length=10, choices=Estado.choices, null=False)

    def indicar_diagnostico(self):
        pass

    def mostrar_nombre(self):
        return self.nombre

    def sugerir_alimento(self):
        pass

class Jaula(models.Model):
    capacidad = models.IntegerField()
    contador = models.IntegerField()
    esta_limpio = models.BooleanField()
    numero_jaula = models.CharField(max_length=50)
    animales = models.ManyToManyField(Animal, related_name='jaulas')

    def agregar_animal(self):
        pass

    def mostrar_numero_jaula(self):
        return self.numero_jaula

class Empleado(models.Model):
    contador = models.IntegerField()
    identificacion = models.IntegerField()
    salario = models.FloatField()

    def mostrar_identificacion(self):
        return self.identificacion

class Cuidador(Empleado):
    def cuidar_animal(self):
        pass

    def dar_comida(self):
        pass

class Veterinario(Empleado):
    especialidad = models.CharField(max_length=255)

    def realizar_diagnostico(self):
        pass

    def realizar_tratamiento(self):
        pass

    def verificar_especialidad(self):
        pass

class PersonalAdministrativo(Empleado):
    def gestionar_recursos(self):
        pass

class PersonalLimpieza(Empleado):
    def limpiar_jaula(self):
        pass

class Cliente(models.Model):
    cedula = models.CharField(max_length=20)
    edad = models.IntegerField()

    def comprar_boleto(self):
        pass

    def listar_informacion(self):
        return f"Cédula: {self.cedula}, Edad: {self.edad}"

class Guia(Empleado):
    clientes = models.ManyToManyField(Cliente, related_name='guias')

    def agregar_cliente(self):
        pass

    def establecer_recorrido(self):
        pass

    def mostrar_cliente(self):
        pass

class Boleto(models.Model):
    contador = models.IntegerField()
    fecha_visita = models.DateField()
    numero = models.IntegerField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='boletos')

class Compra(models.Model):
    contador = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')

    def agregar_cliente(self):
        pass

    def calcular_total(self):
        pass

    def mostrar_total_boletos(self):
        pass

class HistorialMedico(models.Model):
    diagnostico = models.TextField()
    fecha = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='historial_medico')

    def registro_clinico(self):
        return f"Diagnóstico: {self.diagnostico} ({self.fecha})"
