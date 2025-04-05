from django.urls import path,include 
from VentasApp.views import (
    listarcategoria, agregarcategoria, editarcategoria, eliminarcategoria,
    listarunidad, agregarunidad, editarunidad, eliminarunidad,
    listarproducto, agregarproducto, editarproducto, eliminarproducto,
    listarcliente, agregarcliente, editarcliente, eliminarcliente,
    listarventa,agregarventa, por_tipo, encontrar_cliente,producto_codigo,reporte_detalle_venta, eliminarventa, 
    reporte_cliente, reporte_ventas
)
from django.contrib.auth import views

urlpatterns = [ 
                path('listacategoria/',listarcategoria,name="listarcategoria"),
                path('agregarcategoria/',agregarcategoria ,name="agregarcategoria"),
                path('editarcategoria/<int:id>/',editarcategoria ,name="editarcategoria"),
                path('eliminarcategoria/<int:id>/',eliminarcategoria, name='eliminarcategoria'),
                path('listaunidad/',listarunidad,name="listarunidad"),
                path('agregarunidad/',agregarunidad ,name="agregarunidad"),
                path('editarunidad/<int:id>/',editarunidad ,name="editarunidad"),
                path('eliminarunidad/<int:id>/',eliminarunidad, name='eliminarunidad'),
                path('listaproducto/',listarproducto,name="listarproducto"),
                path('agregarproducto/',agregarproducto ,name="agregarproducto"),
                path('editarproducto/<int:id>/',editarproducto ,name="editarproducto"),
                path('eliminarproducto/<int:id>/',eliminarproducto, name='eliminarproducto'),
                path('listarcliente/', listarcliente, name='listarcliente'),
                path('agregarcliente/', agregarcliente, name='agregarcliente'),
                path('editarcliente/<int:id>/', editarcliente, name='editarcliente'),
                path('eliminarcliente/<int:id>/', eliminarcliente, name='eliminarcliente'),
                path('listarventa/', listarventa, name='listarventa'),
                path('agregarventa/', agregarventa, name='agregarventa'),
                path('eliminarventa/<int:id>/', eliminarventa, name='eliminarventa'),
                path('EncontrarCliente/<int:idcliente>/', encontrar_cliente, name='encontrar_cliente'),
                path('reporte-detalle-venta/<int:idventa>/', reporte_detalle_venta, name='reporte_detalle_venta'),
                path('reporte_cliente/<int:cliente_id>/', reporte_cliente, name='reporte_cliente'),
                path('EncontrarProducto/<int:idproductos>/', producto_codigo, name='producto_codigo'),
                path('EncontrarTipo/<int:tipo_id>/', por_tipo, name='por_tipo'),
                path('reporte_ventas/', reporte_ventas, name='reporte_ventas'),

              ]