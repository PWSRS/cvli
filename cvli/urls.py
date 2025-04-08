from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from ocorrencias import views as ocorrencias_views

urlpatterns = [
    path('', RedirectView.as_view(url='/ocorrencias/')),
    path('admin/', admin.site.urls),
    path('ocorrencias/', include('ocorrencias.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', ocorrencias_views.register, name='register'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]
