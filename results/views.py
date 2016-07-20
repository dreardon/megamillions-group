from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Drawing


def index(request):
    allDrawings = Drawing.objects.order_by('-drawingDate')[:20]
    context = {'allDrawings': allDrawings}
    return render(request, 'results/index.html', context)