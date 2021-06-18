from django.contrib import admin
from .models import Clientes, Articulos, Pedidos

# Register your models here.

#clase para mostrar y modificar el model.admin
class ClientesAdmin(admin.ModelAdmin):
    #cammpo para mostrar en lista de admin
    list_display=("nombre","direccion","tfno")
    #campo para colocar casilla de busqueda y especificar q campos buscar
    search_fields=("nombre","tfno")

class ArticulosAdmin(admin.ModelAdmin):
    #campo para mostrar en lista de admin
    list_display=("nombre", "seccion", "precio")
    #campo para agregar filtro en el panel admin
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
