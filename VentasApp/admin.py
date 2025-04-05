from django.contrib import admin
from .models import Categoria, Unidad, Producto, Cliente

# Registra cada modelo para que aparezca en el panel de administración
admin.site.register(Categoria)
admin.site.register(Unidad)
admin.site.register(Producto)
admin.site.register(Cliente)
# admin.site.register(CabeceraVenta)
# admin.site.register(DetalleVenta)
# admin.site.register(Tipo)
# admin.site.register(Parametro)
