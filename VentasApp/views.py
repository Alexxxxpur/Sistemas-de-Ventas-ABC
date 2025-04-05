from django.shortcuts import render,redirect, get_object_or_404 
from VentasApp.models import Categoria,Unidad,Producto,Cliente,CabeceraVenta,DetalleVenta,Tipo,Parametro
from django.db.models import Q 
from .forms import CategoriaForm,UnidadForm,ProductoForm,ClienteForm
from django.http import JsonResponse,HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.db import transaction
from django.core.paginator import Paginator
from datetime import datetime
from datetime import timedelta
from django.db.models import Sum

#  C A T E G O R I A S
def listarcategoria(request):
    queryset = request.GET.get("buscar")
    categoria = Categoria.objects.filter(estado=True) 
    if queryset:
        categoria = Categoria.objects.filter(Q(descripcion__icontains=queryset), estado=True).distinct() 
    
    paginator = Paginator(categoria, 5)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'categoria': categoria, 'page_obj': page_obj}
    return render(request, "categoria/listar.html", context)
def agregarcategoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaForm()
    
    context = {'form': form}
    return render(request, "categoria/agregar.html", context)

def editarcategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {"form": form}
    return render(request, "categoria/editar.html", context)

def eliminarcategoria(request,id):
    categoria=Categoria.objects.get(id=id)
    categoria.estado=False
    categoria.save()
    return redirect("listarcategoria")

#  U N I D A D
def listarunidad(request):
    queryset = request.GET.get("buscar")
    unidad = Unidad.objects.filter(estado=True) 
    if queryset:
        unidad = Unidad.objects.filter(Q(descripcion__icontains=queryset), estado=True).distinct() 
    
    paginator = Paginator(unidad, 5)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'unidad': unidad, 'page_obj': page_obj}

    return render(request, "unidad/listar.html", context)
def agregarunidad(request):
    if request.method == "POST":
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarunidad")
    else:
        form = UnidadForm()
    
    context = {'form': form}
    return render(request, "unidad/agregar.html", context)

def editarunidad(request, id):
    unidad = Unidad.objects.get(id=id)
    if request.method == "POST":
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect("listarunidad")
    else:
        form = UnidadForm(instance=unidad)
    
    context = {"form": form}
    return render(request, "unidad/editar.html", context)

def eliminarunidad(request,id):
    unidad=Unidad.objects.get(id=id)
    unidad.estado=False
    unidad.save()
    return redirect("listarunidad")

# P R O D U C T O S 
def listarproducto(request):
    queryset = request.GET.get("buscar")
    producto = Producto.objects.filter(estado=True) 
    if queryset:
        producto = Producto.objects.filter(Q(descripcion__icontains=queryset), estado=True).distinct() 
    
    paginator = Paginator(producto, 5)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'productos': producto, 'page_obj': page_obj}
    return render(request, "producto/listar.html", context)

def agregarproducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarproducto")
    else:
        form = ProductoForm()
    
    context = {'form': form}
    return render(request, "producto/agregar.html", context)

def editarproducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("listarproducto")
    else:
        form = ProductoForm(instance=producto)
    
    context = {"form": form}
    return render(request, "producto/editar.html", context)

def eliminarproducto(request,id):
    producto=Producto.objects.get(id=id)
    producto.estado=False
    producto.save()
    return redirect("listarproducto")

# C L I E N T E
def listarcliente(request):
    buscar_nombre = request.GET.get("buscar_nombre")
    buscar_dni = request.GET.get("buscar_dni")

    # Inicialmente filtra solo por estado activo
    cliente = Cliente.objects.filter(estado=True)

    if buscar_nombre:
        cliente = cliente.filter(nombres__icontains=buscar_nombre)

    if buscar_dni:
        cliente = cliente.filter(ruc_dni__icontains=buscar_dni)
    
    paginator = Paginator(cliente, 5)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'clientes': cliente, 'page_obj': page_obj}
    return render(request, "cliente/listar.html", context)


def agregarcliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarcliente")
    else:
        form = ClienteForm()
    
    context = {'form': form}
    return render(request, "cliente/agregar.html", context)

def editarcliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("listarcliente")
    else:
        form = ClienteForm(instance=cliente)
    
    context = {"form": form}
    return render(request, "cliente/editar.html", context)

def eliminarcliente(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.estado=False
    cliente.save()
    return redirect("listarcliente")

#   V E N T A S
def listarventa(request):
    queryset = request.GET.get("buscar")
    venta = CabeceraVenta.objects.filter(estado=True) 
    if queryset:
        venta = CabeceraVenta.objects.filter(Q(id__icontains=queryset), estado=True).distinct() 
    
    paginator = Paginator(venta, 5)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'ventas': venta, 'page_obj': page_obj}
    return render(request, "venta/listar.html", context)
    

def agregarventa(request):
    clientes = Cliente.objects.filter(estado=True)
    productos = Producto.objects.filter(estado=True)
    tipo = Tipo.objects.all()

    if request.method == 'POST':
        idtipo = request.POST.get('seltipo')  # Asegúrate de que este campo exista en tu formulario
        idcliente = request.POST.get('idcliente')

        # Validar que idcliente e idtipo no sean vacíos
        if idtipo and idcliente:
            tipo_instance = get_object_or_404(Tipo, id=idtipo)
            cliente_instance = get_object_or_404(Cliente, id=idcliente)

            # Obtener valores de los campos del formulario
            fechaventa = request.POST.get('fecha')
            nrodoc = request.POST.get('nrodoc')
            total = float(request.POST.get('total'))

            if idtipo=='1':
                igv=0
                subtotal=total
            else:
                igv=total*0.18
                subtotal=total-igv
            try:
                with transaction.atomic():
                    venta = CabeceraVenta(
                        fechaventa=fechaventa,
                        nrodoc=nrodoc,
                        total=total,
                        igv=igv,
                        subtotal=subtotal,
                        estado=True,
                        cliente=cliente_instance,
                        tipo=tipo_instance
                    )
                    venta.save()
                    producto= request.POST.getlist('cod_producto[]')
                    precioventa = request.POST.getlist('pventa[]')
                    cantidad = request.POST.getlist('cantidad[]')


                    for producto_id, precio, cantidad in zip(producto, precioventa, cantidad):
                        producto_instance = get_object_or_404(Producto, id=producto_id)
                        cantidad = int(cantidad)  # Convertir cantidad a entero
                        precio = float(precio)  # Convertir precio a float

                        if producto_instance.stock >= cantidad:
                            producto_instance.stock -= cantidad
                            producto_instance.save()

                            detalle = DetalleVenta(
                                iddetalle=venta,
                                productos=producto_instance,
                                precio=precio,
                                cantidad=cantidad
                            )
                            detalle.save()
                        else:
                            print(f'Error: Stock insuficiente para el producto {producto_id}')
                            # Maneja el caso de stock insuficiente, posiblemente mostrando un mensaje al usuario

                        
                    return redirect('listarventa')  # Redirige a una URL de éxito o muestra un mensaje
            
            except Exception as e:
                print(f'Error al guardar la venta: {e}')
                # Maneja el error y muestra un mensaje de error si es necesario

        else:
            print('ID de tipo o cliente vacío')
            # Maneja el caso cuando idcliente o idtipo están vacíos

    context = {'clientes': clientes, 'tipos': tipo, 'productos': productos}
    return render(request, 'venta/agregar.html', context)

def eliminarventa(request, id):
    venta = CabeceraVenta.objects.get(id=id)
    detalles = DetalleVenta.objects.filter(iddetalle=venta)

    try:
        with transaction.atomic():
            # Restablecer los stocks de los productos
            for detalle in detalles:
                producto = detalle.productos
                producto.stock += detalle.cantidad
                producto.save()

            # Cambiar el estado de la venta a False (eliminada)
            venta.estado = False
            venta.save()

    except Exception as e:
        print(f'Error al eliminar la venta: {e}')
        # Maneja el error y muestra un mensaje de error si es necesario

    return redirect("listarventa")


def reporte_detalle_venta(request, idventa):
    venta = get_object_or_404(CabeceraVenta, id=idventa)
    detalles = venta.detalles.all()

    # Crear una lista de detalles con el total calculado
    detalles_con_total = []
    for detalle in detalles:
        total_producto = detalle.precio * detalle.cantidad
        detalles_con_total.append({
            'id': detalle.productos.id,
            'descripcion': detalle.productos.descripcion,
            'cantidad': detalle.cantidad,
            'precio': detalle.precio,
            'total': total_producto
        })

    # Calcular el total general
    total_general = sum(item['total'] for item in detalles_con_total)

    context = {
        'venta': venta,
        'detalles': detalles_con_total,
        'total_general': total_general
    }

    # return render(request, 'venta/reporte_detalle_venta.html', context)
    template = 'venta/reporte_detalle_venta.html'
    html = render(request, template, context).content.decode('utf-8')

    # Convertir el HTML a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Detalle_Venta_{venta.id}.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=result)

    if not pdf.err:
        response.write(result.getvalue())
        return response
    else:
        return HttpResponse('Error al generar el PDF', status=500)
    
def reporte_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    ventas = cliente.ventas().order_by('fechaventa')
    
    # Calcular el total general
    total_general = sum(venta.total for venta in ventas)
    
    context = {
        'cliente': cliente,
        'ventas': ventas,
        'total_general': total_general,
    }
    template = 'cliente/reporte_cliente.html'
    html = render(request, template, context).content.decode('utf-8')

    # Convertir el HTML a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Reporte_Cliente_{cliente.id}.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=result)

    if not pdf.err:
        response.write(result.getvalue())
        return response
    else:
        return HttpResponse('Error al generar el PDF', status=500)
    

def reporte_ventas(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    ventas = CabeceraVenta.objects.filter(fechaventa__range=[start_date, end_date])
    total_ventas = ventas.aggregate(Sum('total'))['total__sum'] or 0


    context = {
         'ventas': ventas,
        'total_ventas': total_ventas,
        'start_date': start_date,
        'end_date': end_date
    }

    template = 'venta/reporte_ventas.html'
    html = render(request, template, context).content.decode('utf-8')

    # Convertir el HTML a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Reporte_ventas.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=result)

    if not pdf.err:
        response.write(result.getvalue())
        return response
    else:
        return HttpResponse('Error al generar el PDF', status=500)

def encontrar_cliente(request, idcliente):
    try:
        cliente = Cliente.objects.get(id=idcliente)
        data = {
            'ruc_dni': cliente.ruc_dni,
            'direccion': cliente.direccion,
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

def producto_codigo(request, idproductos):
    try:
        producto = Producto.objects.get(id=idproductos)
        data = {
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'unidad': producto.unidad.descripcion,  # Suponiendo que `descripcion` es un campo en `Unidad`
            'categoria': producto.categoria.descripcion  # Suponiendo que `descripcion` es un campo en `Categoria`
        }
        return JsonResponse(data)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    except Exception as e:
        print(f'Error: {e}')  # Imprime el error en la terminal para depuración
        return JsonResponse({'error': 'Error interno del servidor'}, status=500)

def por_tipo(request,tipo_id):
    try:
        resultados = (
            Parametro.objects
            .filter(tipo_id=tipo_id)
            .values('tipo_id', 'serie', 'numeracion')
        )
        return JsonResponse(list(resultados), safe=False)
    except Exception as e:
        print(f'Error: {e}')  # Imprime el error en la terminal para depuración
        return JsonResponse({'error': 'Error interno del servidor'}, status=500)