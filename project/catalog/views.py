# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Product


def catalog(request):
    products = Product.objects.all()

    return render_to_response(
        'catalog.html',
        {
            'products': products,
        },
        context_instance=RequestContext(request)
    )