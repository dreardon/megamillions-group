from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from .models import Drawing, PrizesWon, GroupTicket


def index(request):
    allDrawings = Drawing.objects.order_by('-drawingDate')[:50]
    allPrizes = PrizesWon.objects.order_by('drawing_id')
    activeTickets = GroupTicket.objects.order_by('-numbers')
    toBePaid = PrizesWon.objects.aggregate(Sum('groupPrizeAmount'))
    paidOut = 0
    all_objects = list(PrizesWon.objects.all())
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