"""gestion_reclamos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [

    # Django Admin Path
    path('admin-django/', admin.site.urls),

    # Django Custom App Paths
    path('', include('apps.base.urls')),
    path('reclamos/', include('apps.reclamos.urls')),
    path('inspeccion/',include('apps.inspeccion.urls')),
    path('gestion/', include('apps.gestion.urls')),
    path('admin/', include('apps.administracion.urls')),

    path('logout/', views.logout_page.as_view(), name='logout-page'),

    # Django Accounts Paths
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/_login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(
        template_name='registration/_logged_out.html'), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/_password_change_form.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/_password_change_done.html'), name='password_change_done'),
    # path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='base/index.html'), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/_password_reset_form.html',
        email_template_name = 'registration/_password_reset_email.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/_password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/_password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/_password_reset_complete.html'), name='password_reset_complete'),
    # path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='registration/_login.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
