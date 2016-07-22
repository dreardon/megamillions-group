from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Drawing, PrizesWon


def index(request):
    allDrawings = Drawing.objects.order_by('-drawingDate')[:50]
    allPrizes = PrizesWon.objects.order_by('-drawing')
    toBePaid = PrizesWon.objects.aggregate(Sum('groupPrizeAmount'))
    context = {'allDrawings': allDrawings, 'allPrizes': allPrizes, 'toBePaid':toBePaid}
    return render(request, 'results/index.html', context)