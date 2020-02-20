from django.contrib import admin
from .models import *
# Register your models here.

class TableroAdmin(admin.ModelAdmin):
    display=('nombre')

admin.site.register(Tablero,TableroAdmin)

class ListaAdmin(admin.ModelAdmin):
    list_display=('nombreLista', 'fkTablero')

admin.site.register(Lista,ListaAdmin)

class TareaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'descripcion', 'fkLista')
admin.site.register(Tarea,TareaAdmin)


