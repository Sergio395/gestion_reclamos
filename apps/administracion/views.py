# from datetime import datetime
# from django.http import HttpResponse
# from django.template import loader
from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from .forms import Userform, AdminForm, Nuevaform ,Newuserform, Edituserform, Empresaform, OrdencompraForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empresa, OrdenCompra, Usuario
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required



@login_required
def admin(request):
    return render(request, 'administracion/admin_index.html', {})


"""
    IMPLEMENTACION DE CRUD DE CATEGORIA POR MEDIO DE VISTAS BASADAS EN CLASES (VBC)
"""

#------------------------------------crud usuario-----------------------------------------------------------------------   

class UserListView(mixins.LoginRequiredMixin, ListView):
    model = Usuario
    context_object_name = 'users'
    template_name = 'administracion/usuarios.html'
    queryset = Usuario.objects.filter(eliminado=False)
    #ordering = ['apellido']


class UserCreateView(mixins.LoginRequiredMixin,CreateView):
    model = Usuario
    form_class = Userform
    template_name = 'administracion/nuevo_usuario.html'
    success_url = reverse_lazy('usuario')
    
 

class UserUpdateView(mixins.LoginRequiredMixin, UpdateView):
    
    model = Usuario
    form_class = Userform
    template_name = 'administracion/edit_usuario.html'
    success_url = reverse_lazy('usuario')
    
    #Si queremos sobrescribir la obtención del objeto
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Usuario, pk=pk)        
        return obj
    
    def post(self, request,*args,**kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg) 
        usuario = Usuario.objects.get(pk=pk)
        formulario = Userform(request.POST or None, request.FILES or None, instance=usuario)
        
        if Usuario.eliminado == True:
            messages.warning(request, 'El registro ha sido eliminado de la base de datos')      
            return redirect('usuario')

        if formulario.is_valid():
            formulario.save()
            messages.success(self.request, 'Se ha editado el usuario correctamente')            
            return redirect('usuario')
        
@login_required     
def delete_usuario(request,pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    usuario.soft_delete()
    messages.warning(request, 'Se ha eliminado  el registro correctamente')
    return redirect('usuario')




#------------------------------------inicio crud empresa---------------------------------------------------------------------------

class ListarEmpresas(mixins.LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'administracion/empresas.html'
    context_object_name = 'proveedores'    
    queryset = Empresa.objects.filter(eliminado=False)
    

@login_required
def nueva_empresa(request):


    if (request.method == 'POST'):
        
        formulario = Nuevaform(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Proveedor creado correctamente')
            return redirect('empresa')
            
    else:
        formulario = Nuevaform()
    return render(request, 'administracion/nueva_empresa.html', {'empresaform': formulario})

@login_required
def editar_empresa(request, id_empresa):
    
    try:
        empresa = Empresa.objects.get(pk=id_empresa)
    except Empresa.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    formulario = Nuevaform(request.POST or None, request.FILES or None, instance=empresa)
    if empresa.eliminado == True:
        messages.warning(request, 'El registro ha sido eliminado de la base de datos')      
        return redirect('empresa')
        
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha editado el proveedor correctamente')
        return redirect('empresa')
        
       
          
    return render(request, 'administracion/edit_empresa.html', {'empresaform': formulario, 'ID' : id_empresa})



@login_required
def delete_empresa(request, id_empresa):
    try:
        empresa = Empresa.objects.get(pk=id_empresa)
    except Empresa.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    empresa.soft_delete()
    messages.warning(request, 'Se ha eliminado  el registro correctamente')
    return redirect('empresa')




#------------------------------------inicio crud OC------------------------------------------------------------------------------


class OrdencompraListView(mixins.LoginRequiredMixin, ListView):
    model = OrdenCompra
    context_object_name = 'oc'
    template_name = 'administracion/ordenes_compra.html'
    queryset = OrdenCompra.objects.filter(eliminado=False)
    ordering = ['numero']


class OrdencompraCreateView(mixins.LoginRequiredMixin, CreateView):
    model = OrdenCompra
    fields = '__all__'
    #form_class = OrdencompraForm
    template_name = 'administracion/nueva_oc.html'
    success_url = reverse_lazy('orden_compra')
    
    

class OrdencompraUpdateView(mixins.LoginRequiredMixin, UpdateView):
    model = OrdenCompra
    fields = '__all__'    
    exclude=['eliminado']
    
    # form_class = CategoriaForm
    template_name = 'administracion/editar_oc.html'
    success_url = reverse_lazy('orden_compra')

    #Si queremos sobrescribir la obtención del objeto
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(OrdenCompra, pk=pk)        
        return obj
    
    def mensaje(self,request):
        messages.warning(request, 'Se ha editado  el registro correctamente')
    

@login_required
def delete_oc(request, pk):
    try:
        oc = OrdenCompra.objects.get(pk=pk)
    except OrdenCompra.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    oc.soft_delete()
    messages.warning(request, 'Se ha eliminado  el registro correctamente')
    return redirect('orden_compra')




































# class OrdencompraDeleteView(DeleteView):
    # model = OrdenCompra
    # template_name = 'administracion/ordenes_compra.html'
    # success_url = reverse_lazy('orden_compra')

    # #Si queremos sobrescribir la obtención del objeto
    # def get_object(self, queryset=None):
        # pk = self.kwargs.get(self.pk_url_kwarg)
        # obj = get_object_or_404(OrdenCompra, pk=pk)
        # return obj

    # # se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
    # def delete(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # self.object.soft_delete()  # Llamada al método soft_delete() del modelo
        # return HttpResponseRedirect(self.get_success_url())

#----------------------------------------------------------------------------------------------------------------------------








# def nuevo_usuario(request):
    # mensaje = None
    # if request.method == 'POST':
        # nuevo_usuario_form = Newuserform(request.POST)
        # mensaje = 'Hemos recibido tus datos'

    # elif request.method == 'GET':
        # nuevo_usuario_form = Newuserform()
    # else:
        # return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {

        # 'mensaje': mensaje,
        # 'nuevo_usuario': nuevo_usuario_form
    # }
    # return render(request, 'administracion/nuevo_usuario.html', context)
# # -----------------------------------------------------------------------------------------------------------------------------


# def nueva_empresa(request):

    # mensaje = None
    # if request.method == 'POST':
        # nueva_form = Nuevaform(request.POST)
        # mensaje = 'Hemos recibido tus datos'
    # elif request.method == 'GET':
        # nueva_form = Nuevaform()
    # else:
        # return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {

        # 'mensaje': mensaje,
        # 'nueva_form': nueva_form
    # }
    # return render(request, 'administracion/nueva_empresa.html', context)


# def edit_usuario(request, usuario_num):
    # users = [("Chavodelocho", "Chavo", "delocho", 8888, "Admin", 14000),
            #  ("kiko", "Federdo", "Garcia", 3333, "Inspector", 14001),
            #  ("candelaylamoto?", "Candela", "Moto", 2222, "Gestor", 14002),
            #  ("chilindrina", "Chili", "Peppers", 1111, "basico", 14003)]
    # lista = users[usuario_num - 1]
    # mensaje = None
    # if request.method == 'POST':
        # edit_usuario_form = Edituserform(request.POST)
        # mensaje = 'Hemos recibido tus datos'

    # elif request.method == 'GET':
        # edit_usuario_form = Edituserform()
    # else:
        # return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {
        # 'usuario': lista,
        # 'mensaje': mensaje,
        # 'edit_usuario': edit_usuario_form
    # }
    # return render(request, 'administracion/edit_usuario.html', context)
# -----------------------------------------------------------------------------------------------------------------------------


# def delete_usuario(request, usuario_num):
    # users = [("Chavodelocho", "Chavo", "delocho", 8888, "Admin", 14000),
            #  ("kiko", "Federdo", "Garcia", 3333, "Inspector", 14001),
            #  ("candelaylamoto?", "Candela", "Moto", 2222, "Gestor", 14002),
            #  ("chilindrina", "Chili", "Peppers", 1111, "basico", 14003)]
    # del users[usuario_num-1]

    # mensaje = None
    # if request.method == 'POST':
        # User_form = Userform(request.POST)
        # mensaje = 'Hemos recibido tus datos'
    # elif request.method == 'GET':
        # User_form = Userform()
    # else:
        # return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {
        # 'users': users,
        # 'mensaje': mensaje,
        # 'Userform': User_form
    # }
    # return render(request, 'administracion/usuarios.html', context)
# # --------------------------------------------------------------------------------------------------------------------------




# def empresa(request):
    # proveedores = [("La podadora", "La podadora S.A.", "1456", "20303406022", "lapodadora@gmail.com", "155202636"),
                #    ("La podadora", "La podadora S.A.", "1456",
                    # "20303406022", "lapodadora@gmail.com", "155202636"),
                #    ("La podadora", "La podadora S.A.", "1456",
                    # "20303406022", "lapodadora@gmail.com", "155202636"),
                #    ("La podadora", "La podadora S.A.", "1456",
                    # "20303406022", "lapodadora@gmail.com", "155202636"),
                #    ("La podadora", "La podadora S.A.", "1456",
                    # "20303406022", "lapodadora@gmail.com", "155202636"),
                #    ("La podadora", "La podadora S.A.", "1456", "20303406022", "lapodadora@gmail.com", "155202636")]
    # mensaje = None
    # if request.method == 'POST':
        # empresa_form = Empresaform(request.POST)
        # mensaje = 'Hemos recibido tus datos'

    # elif request.method == 'GET':
        # empresa_form = Userform()
    # else:
        # return HttpResponseNotAllowed(f"Método {request.method} no soportado")

    # context = {
        # 'proveedores': proveedores,
        # 'mensaje': mensaje,
        # 'empresaform': empresa_form
    # }
    # return render(request, 'administracion/empresas.html', context)