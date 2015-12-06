# coding: utf-8
from django.template import RequestContext
from django.http import JsonResponse
from django.shortcuts import render_to_response
import lxml.html
import urllib2


def clear_str(str):
    return str.replace('\r', '').replace('\t', '').replace('\n', '')


def home(request):
    return render_to_response(
        'home.html',
        {},
        context_instance=RequestContext(request)
    )


def parse(request):
    page = urllib2.urlopen(request.GET['url'])
    doc = lxml.html.document_fromstring(page.read())

    name = doc.cssselect('#name')[0]
    type = doc.cssselect('#type')[0]
    price = doc.cssselect('#price1')[0]
    marking = doc.cssselect('#itemNumber')[0]
    description = doc.cssselect('#salesArg')[0]

    return JsonResponse({
        'name': clear_str(name.text),
        'type':  clear_str(type.text),
        'price':  clear_str(price.text)[0:-3],
        'marking':  clear_str(marking.text),
        'description':  clear_str(description.text),
    })