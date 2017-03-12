from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from datetime import date
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from .models import Drawing, PrizesWon, GroupTicket, PaidOut, AgreementPeriod


def index(request):
    currentPeriod = AgreementPeriod.objects.filter(startDate__lte=date.today(), endDate__gte=date.today())
    allCurrentDrawings = Drawing.objects.filter(drawingDate__lte=date.today(), drawingDate__gte=currentPeriod.first().startDate).order_by('-drawingDate')
    allHistoricalDrawings = Drawing.objects.filter(drawingDate__lte=currentPeriod.first().startDate).order_by('-drawingDate')[:50]
    allCurrentPrizes = PrizesWon.objects.filter(ticket__agreementPeriod=currentPeriod).order_by('-drawing__drawingDate')
    allHistoricalPrizes = PrizesWon.objects.exclude(ticket__agreementPeriod=currentPeriod).order_by('-drawing__drawingDate')
    activeTickets = GroupTicket.objects.filter(agreementPeriod=currentPeriod).order_by('-numbers')
    toBePaid = PrizesWon.objects.filter(ticket__agreementPeriod=currentPeriod).aggregate(Sum('groupPrizeAmount'))
    paidOut = PaidOut.objects.aggregate(Sum('prizeAmount'))
    context = {'allCurrentDrawings': allCurrentDrawings, 'allHistoricalDrawings':allHistoricalDrawings, 'allCurrentPrizes': allCurrentPrizes, 'allHistoricalPrizes': allHistoricalPrizes, 'toBePaid':toBePaid, 'activeTickets':activeTickets,'paidOut':paidOut,'currentPeriod':currentPeriod.first()}
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