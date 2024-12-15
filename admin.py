from django.contrib import admin
from .models import (
    Direccion, Zoologico, SerVivo, Animal, Jaula, Empleado,
    Cuidador, Veterinario, PersonalAdministrativo, PersonalLimpieza,
    Cliente, Guia, Boleto, Compra, HistorialMedico
)

# Registro de los modelos
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle_principal', 'calle_secundaria', 'referencia')
    search_fields = ('calle_principal', 'calle_secundaria')

@admin.register(Zoologico)
class ZoologicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'capacidad')
    search_fields = ('nombre',)

@admin.register(SerVivo)
class SerVivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento')
    search_fields = ('nombre',)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_cientifico', 'peso', 'tipo_dieta', 'estado')
    list_filter = ('tipo_dieta', 'tipo_cuerpo', 'estado')
    search_fields = ('nombre', 'nombre_cientifico')

@admin.register(Jaula)
class JaulaAdmin(admin.ModelAdmin):
    list_display = ('numero_jaula', 'capacidad', 'contador', 'esta_limpio')
    list_filter = ('esta_limpio',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'salario')
    search_fields = ('identificacion',)

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'salario')

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'especialidad', 'salario')
    search_fields = ('especialidad',)

@admin.register(PersonalAdministrativo)
class PersonalAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'salario')

@admin.register(PersonalLimpieza)
class PersonalLimpiezaAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'salario')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'edad')
    search_fields = ('cedula',)

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'salario')

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha_visita', 'valor', 'cliente')
    list_filter = ('fecha_visita',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('contador', 'cliente')

@admin.register(HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('diagnostico', 'fecha', 'animal')
    list_filter = ('fecha',)
    search_fields = ('diagnostico',)
