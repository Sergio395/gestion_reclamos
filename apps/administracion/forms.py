# from django.contrib.admin import widgets
from django import forms
from .models import Empresa, OrdenCompra, Usuario


class AdminForm(forms.Form):
    pass


class Userform(forms.ModelForm):
    class Meta:
        model = Usuario
        #fields='__all__'
        fields = ['usuario','nombre','apellido','legajo','correo_electronico','clave','permiso']
        # exclude=('baja',)
        # usuario = forms.CharField (label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
        # password= forms.CharField (label='Contraseña', widget=forms.RadioSelect(
        # attrs={'class': 'col'}), choices='')
        # permisos= forms.CharField (label='Inspector designado',
        # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})


class Empresaform(forms.ModelForm):
    pass
    # class Meta:
        # model = Empresa
        # fields='__all__'






class Nuevaform(forms.ModelForm):
    
    class Meta:
        model = Empresa
        # fields='__all__'
        fields = ['fecha_alta','nombre','razon_social','num_proveedor','cuit','correo','telefono','orden_compra']
        # exclude=('baja',)
        # widgets = {
        # #    'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre'})
            # 'fecha_alta' : forms.DateField(attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}),
                # #attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # 'nombre' : forms.TextInput(label='Nombre', max_length=20, widget=forms.TextInput( 
                # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # # 'razon_social' : forms.TextInput(label='Razón social',  max_length=30, widget=forms.TextInput(
                # # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # 'num_proveedor' : forms.IntegerField(label='N° proveedor', widget=forms.TextInput(
                # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # 'cuit' : forms.TextInput(label='N° Cuit', max_length=9, min_length=9, widget=forms.TextInput(
                # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # 'correo' : forms.EmailField(label='Correo', widget=forms.TextInput(
                # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # 'telefono' : forms.IntegerField(label='Telefono', widget=forms.TextInput(
                # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'})),
            # 'orden_compra' : forms.TextInput(label='N° Cuit', max_length=9, min_length=9, widget=forms.TextInput(
                # attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
                        

class OrdencompraForm(forms.ModelForm):
    
    class Meta:
        model = OrdenCompra
        fields = '__all__'
        exclude = ('eliminado',)










class Newuserform(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    nombre = forms.CharField(label='Nombre', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    apellido = forms.CharField(label='Apellido',  max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    contra = forms.IntegerField(label='Contraseña', widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    permiso = forms.CharField(label='Permisos', max_length=9, min_length=9, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    legajo = forms.EmailField(label='Legajo', widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))


class Edituserform(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    nombre = forms.CharField(label='Nombre', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    apellido = forms.CharField(label='Apellido',  max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    contra = forms.IntegerField(label='Contraseña', widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    permiso = forms.CharField(label='Permisos', max_length=9, min_length=9, widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
    legajo = forms.EmailField(label='Legajo', widget=forms.TextInput(
        attrs={'class': 'form-control  mx-auto', 'style': 'height: 2em;'}))
