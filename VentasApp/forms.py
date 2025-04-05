from django import forms 
from django.forms import inlineformset_factory 
from .models import Categoria,Unidad,Producto,Cliente,CabeceraVenta,DetalleVenta

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']  # Incluye el campo 'idcategoria'
        # widgets = {
        #     'idcategoria': forms.HiddenInput(),  # Oculta el campo 'idcategoria' en el formulario
        # }

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['descripcion', 'estado']  # Incluye todos los campos del modelo
        # widgets = {
        #     'idunidades': forms.HiddenInput(),  # Oculta el campo 'idunidades' en el formulario
        # }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'categoria', 'unidad', 'stock', 'precio', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(estado=1)
        self.fields['unidad'].queryset = Unidad.objects.filter(estado=1)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'email', 'direccion', 'ruc_dni', 'estado']
        error_messages = {
            'ruc_dni': {
                'unique': "Ya existe un cliente con este DNI o RUC.",
            },
        }
        # widgets = {
        #     'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        #     'ruc_dni': forms.TextInput(attrs={'class': 'form-control'}),
        #     'nombres': forms.TextInput(attrs={'class': 'form-control'}),
        # }

# class CabeceraVentaForm(forms.ModelForm):
#     class Meta:
#         model = CabeceraVenta
#         fields = ['fechaventa', 'tipo_id', 'nrodoc', 'total', 'igv', 'subtotal', 'estado', 'idcliente']
#         widgets = {
#             'fechaventa': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'tipo_id': forms.Select(attrs={'class': 'form-control'}),
#             'idcliente': forms.Select(attrs={'class': 'form-control'}),
#             'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'igv': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'subtotal': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }

# class DetalleVentaForm(forms.ModelForm):
#     class Meta:
#         model = DetalleVenta
#         fields = ['idproductos', 'precio', 'cantidad']
#         widgets = {
#             'idproductos': forms.Select(attrs={'class': 'form-control'}),
#             'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# # Formset for handling multiple detalles
# DetalleVentaFormset = inlineformset_factory(CabeceraVenta, DetalleVenta, form=DetalleVentaForm, extra=1)