from django.shortcuts import render


# Create your views here.
def admin(request):
    return render(request, 'administracion/admin_index.html', {})
