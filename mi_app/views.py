from django.shortcuts import render
from django.http import HttpResponse
from .models import MiModelo
import django_tables2 as tables
from xhtml2pdf import pisa
from django.template.loader import get_template

def generar_pdf(request):
    # Obtén los datos de tu modelo (ajusta esto según tus necesidades)
    datos = MiModelo.objects.all()

    # Crea un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mi_pdf.pdf"'

    # Crea una plantilla HTML
    template = get_template('mi_template.html')  # Define la ubicación de tu plantilla HTML

    # Contexto de la plantilla con los datos que deseas mostrar en el PDF
    context = {
        'datos': datos,
    }

    # Renderiza la plantilla con el contexto
    html = template.render(context)

    # Convierte la plantilla HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Si la conversión a PDF fue exitosa, devuelve la respuesta con el PDF generado
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', content_type='text/plain')
    return response
