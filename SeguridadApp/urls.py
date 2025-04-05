"""
URL configuration for SeguridadApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from SeguridadApp.views import acceder,homePage,salir
from django.contrib.auth import views
from VentasApp.views import (eliminarcategoria ,eliminarunidad ,eliminarproducto,eliminarcliente)
# , eliminarventa,
# encontrar_cliente,producto_codigo,por_tipo

urlpatterns = [
    path('', acceder , name = "login"),
    path('home/', homePage , name = "home"),
    path('logout/',salir,name="logout"), 
    # path('eliminarcategoria/<int:idcategoria>/',eliminarcategoria,name="eliminarcategoria"),
    # path('eliminarunidad/<int:idunidades>/',eliminarunidad,name="eliminarunidad"),
    # path('eliminarproducto/<int:idproductos>/',eliminarproducto,name="eliminarproducto"),
    # path('eliminarcliente/<int:idcliente>/', eliminarcliente, name='eliminarcliente'),
    # path('eliminarventa/<int:idventas>/', eliminarventa, name='eliminarventa'),
    # path('EncontrarCliente/<int:idcliente>/', encontrar_cliente, name='encontrar_cliente'),
    # path('EncontrarProducto/<int:idproductos>/', producto_codigo, name='producto_codigo'),
    # path('EncontrarTipo/<int:tipo_id>/', por_tipo, name='por_tipo'),
    # path('ventas/',include('VentasApp.urls')),
]