from django.shortcuts import render

from django.http import HttpResponse
from .models import Investment, Workers
from django.template import loader

def index(request):
    template = loader.get_template('checkuser/index.html')
    context = {
        'users' : Workers.objects.all(),
    }
    return HttpResponse(template.render(context, request))
