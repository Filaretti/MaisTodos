import json

from datetime import datetime

import requests

from django.conf import settings
from django.shortcuts import render
from django.http import (
    JsonResponse, HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotAllowed
)
from django.views.decorators.csrf import csrf_exempt

from .models import Customer, Purchase, Type, Product, SaveRequest

from .utils import ValidCPF

@csrf_exempt
def receive_payload(request):
    if request.method != "POST":
        return HttpResponseNotAllowed("POST")

    authentication_token = request.META.get("HTTP_AUTHORIZATION", "")
    if authentication_token != settings.AUTHENTICATION_TOKEN:
        return JsonResponse({
            "status": "error",
            "message": f"O código de autenticação é inválido"
        }, status=401)
    save_request = SaveRequest()
    save_request.received_api = request.body
    posted_data = json.loads(request.body)
    document = posted_data["customer"]["document"]

    n = ValidCPF(document)
    if not n.validCPF():
        return JsonResponse({
            "status": "error",
            "message": f"CPF inválido"
        }, status=400)

    try:
        customer = Customer.objects.get(document=document)
    except Customer.DoesNotExist:
        customer = Customer()
        customer.document = posted_data["customer"]["document"]
    customer.name = posted_data["customer"]["name"]

    purchase = Purchase()
    try:
        purchase.sold_at = datetime.strptime(posted_data["sold_at"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return JsonResponse({
            "status": "error",
            "message": f"A data de venda é inválida"
        }, status=400)
    purchase.total = float(posted_data["total"])

    total_items = 0
    total_cashback = 0
    products = []
    for product_data in posted_data["products"]:
        try:
            type_ = Type.objects.get(name=product_data["type"])
        except Type.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": f"O tipo informado ({product_data['type']}) não corresponde a nenhum tipo existente)"
            }, status=400)
        product = Product()
        product.type = type_
        product.value = float(product_data["value"])
        product.qty = int(product_data["qty"])
        total_value = product.value * product.qty
        calculated_cashback = total_value * (type_.percentage_cashback / 100)

        total_items += total_value
        total_cashback += calculated_cashback

        # List of products not saved yet
        products.append(product)

    if purchase.total != total_items:
        return JsonResponse({
            "status": "error",
            "message": f"O total informado ({purchase.total}) não bate com a soma dos itens na compra ({total_items})"
        }, status=400)

    customer.save()

    purchase.customer = customer
    purchase.save()
    for product in products:
        product.purchase = purchase
        product.customer = customer
        product.save()

    data = {
        "document": customer.document,
        "cashback": total_cashback
    }

    response = requests.post("https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback", json=data)
    save_request.response_api_maistodos = response.text
    save_request.save()

    return JsonResponse({"status": "ok", "purchase": purchase.id})
