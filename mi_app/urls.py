from . import views
from django.urls import include, path

urlpatterns = [
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
   
]
