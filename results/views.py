from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Drawing, PrizesWon, GroupTicket


def index(request):
    allDrawings = Drawing.objects.order_by('-drawingDate')[:50]
    allPrizes = PrizesWon.objects.order_by('-drawing')
    activeTickets = GroupTicket.objects.order_by('-numbers')
    toBePaid = PrizesWon.objects.aggregate(Sum('groupPrizeAmount'))
    paidOut = 0
    context = {'allDrawings': allDrawings, 'allPrizes': allPrizes, 'toBePaid':toBePaid, 'activeTickets':activeTickets,'paidOut':paidOut}
    return render(request, 'results/index.html', context)