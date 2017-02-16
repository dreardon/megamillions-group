from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from .models import Drawing, PrizesWon, GroupTicket, PaidOut


def index(request):
    allDrawings = Drawing.objects.order_by('-drawingDate')[:50]
    allPrizes = PrizesWon.objects.order_by('-drawing__drawingDate')
    activeTickets = GroupTicket.objects.filter(active=True).order_by('-numbers')
    toBePaid = PrizesWon.objects.filter(ticket__active=True).aggregate(Sum('groupPrizeAmount'))
    paidOut = PaidOut.objects.aggregate(Sum('prizeAmount'))
    context = {'allDrawings': allDrawings, 'allPrizes': allPrizes, 'toBePaid':toBePaid, 'activeTickets':activeTickets,'paidOut':paidOut}
    return render(request, 'results/index.html', context)


@csrf_protect
def matchingTickets(request,drawingid,ticketid):
    a = Drawing.objects.get(pk=drawingid)
    b = GroupTicket.objects.get(pk=ticketid)
    return HttpResponse(str(a)+str(b))


@csrf_protect
def results(request,drawingid):
    a = Drawing.objects.get(pk=drawingid)
    return HttpResponse(str(a))