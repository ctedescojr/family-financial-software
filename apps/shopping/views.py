from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from shopping.models import Invoice
import pytesseract
from PIL import Image

import json
import os


@csrf_exempt
@api_view(["POST"])
def upload_invoice(request):
    if "file" not in request.FILES:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    file = request.FILES["file"]
    invoice = Invoice.objects.create(image=file)

    # Processamento OCR
    img_path = invoice.image.path
    text_data = pytesseract.image_to_string(Image.open(img_path))

    # Aqui faremos o parse dos dados (em uma etapa futura, integração com AI)
    products = parse_invoice_data(text_data)

    # Retorno para o Frontend
    return JsonResponse({"producsts": products}, status=200)


def parse_invoice_data(text_data):
    # Função simples para parse inicial
    lines = text_data.split("\n")
    products = []
    for line in lines:
        if len(line.strip()) > 0:
            products.append(
                {
                    "name": line,
                    "price": "0.00",  # Ajustaremos isso com AI na próxima fase
                }
            )
    return products
