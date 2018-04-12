from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from django.views.decorators.csrf import csrf_protect
from .models import Drawing, PrizesWon, GroupTicket, PaidOut, AgreementPeriod


def index(request):
    currentPeriod = AgreementPeriod.objects.order_by('-startDate')[0]
    lastPeriod = AgreementPeriod.objects.order_by('-startDate')[1]
    allCurrentDrawings = Drawing.objects.filter(drawingDate__lte=currentPeriod.endDate, drawingDate__gte=currentPeriod.startDate).order_by('-drawingDate')
    allCurrentPrizes = PrizesWon.objects.filter(ticket__agreementPeriod=currentPeriod).order_by('-drawing__drawingDate')
    allHistoricalDrawings = Drawing.objects.filter(drawingDate__lte=currentPeriod.startDate).order_by('-drawingDate')[:50]
    allHistoricalPrizes = PrizesWon.objects.exclude(ticket__agreementPeriod=currentPeriod).order_by('-drawing__drawingDate')
    if not allCurrentDrawings:
        allCurrentDrawings = Drawing.objects.filter(drawingDate__lte=lastPeriod.endDate,drawingDate__gte=lastPeriod.startDate).order_by('-drawingDate')
        allCurrentPrizes = PrizesWon.objects.filter(ticket__agreementPeriod=lastPeriod).order_by('-drawing__drawingDate')
        allHistoricalDrawings = Drawing.objects.filter(drawingDate__lte=lastPeriod.startDate).order_by('-drawingDate')[:50]
        allHistoricalPrizes = PrizesWon.objects.exclude(ticket__agreementPeriod=lastPeriod).order_by('-drawing__drawingDate')
    activeTickets = GroupTicket.objects.filter(agreementPeriod=currentPeriod).order_by('-numbers')
    toBePaid = PrizesWon.objects.filter(ticket__agreementPeriod=currentPeriod).aggregate(Sum('groupPrizeAmount'))
    paidOut = PaidOut.objects.aggregate(Sum('prizeAmount'))
    context = {'allCurrentDrawings': allCurrentDrawings, 'allHistoricalDrawings':allHistoricalDrawings, 'allCurrentPrizes': allCurrentPrizes, 'allHistoricalPrizes': allHistoricalPrizes, 'toBePaid':toBePaid, 'activeTickets':activeTickets,'paidOut':paidOut,'currentPeriod':currentPeriod}
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