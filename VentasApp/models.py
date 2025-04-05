from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=40)
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    ruc_dni = models.CharField(max_length=8, unique=True)  
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'clientes'
        

    def __str__(self):
        return self.nombres
    
    def ventas(self):
        return self.cabeceraventa_set.all()

class Categoria(models.Model):
    # idcategoria=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField(default=True)
    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.descripcion

    def productos(self):
        return self.producto_set.all()
    
class Unidad(models.Model):
    # idunidades = models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField(default=True)
    
    class Meta:
        db_table = 'unidades'

    def __str__(self):
        return self.descripcion

    def productos(self):
        return self.producto_set.all()
    
class Producto(models.Model):
    # idproductos = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.descripcion
    

class Tipo(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipo'

    def __str__(self):
        return self.descripcion

    def ventas(self):
        return self.cabeceraventa_set.all()

class CabeceraVenta(models.Model):
    fechaventa = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nrodoc = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
   
    class Meta:
        db_table = 'cabeceraventas'

    def __str__(self):
        return self.cliente

    def detalleventas(self):
        return self.detalleventa_set.all()


class DetalleVenta(models.Model):
    iddetalle = models.ForeignKey(CabeceraVenta, on_delete=models.CASCADE, related_name='detalles')
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    class Meta:
        db_table = 'detalleventa'


class Parametro(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    numeracion = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    estado= models.BooleanField(default=1)

    class Meta:
        db_table = 'parametros'

    @staticmethod
    def actualizar_numero(id, numeracion):
        try:
            Parametro.objects.filter(tipo_id=id).update(numeracion=numeracion)
            return True
        except Exception as ex:
            return False
        

        
