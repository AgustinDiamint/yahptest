from django.shortcuts import render

from django.http import HttpResponse
from checkusers.models import Investment, Workers
from django.template import loader


def index(request):
    users_list = Workers.objects.all()
    context = {"users_list": users_list}
    return render(request, "checkusers/index.html", context)
