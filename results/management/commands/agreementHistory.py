from django.core.management.base import BaseCommand, CommandError
import requests
import json
from results.models import GroupTicket, AgreementPeriod, PaidOut
from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Command(BaseCommand):
    help = 'Creates the set of default tickets'

    def handle(self, *args, **options):
        AgreementPeriod(periodName="1st",startDate="2016-08-09",endDate="2016-11-16").save()
        AgreementPeriod(periodName="2nd",startDate="2016-11-22",endDate="2017-02-15").save()
        AgreementPeriod(periodName="3rd",startDate="2017-02-20",endDate="2017-08-18").save()
        AgreementPeriod(periodName="4th", startDate="2017-08-20", endDate="2017-10-27").save()
        AgreementPeriod(periodName="5th", startDate="2017-11-28", endDate="2018-05-25").save()
        AgreementPeriod(periodName="6th", startDate="2018-07-17", endDate="2019-01-11").save()
        AgreementPeriod(periodName="7th", startDate="2019-01-22", endDate="2019-07-20").save()

        GroupTicket(numbers='04 08 23 36 50',megaBall=5,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=False).save()
        GroupTicket(numbers='03 07 13 24 40',megaBall=3,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=False).save()
        GroupTicket(numbers='02 08 17 22 39',megaBall=4,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=False).save()
        GroupTicket(numbers='19 27 39 51 75',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=False).save()
        GroupTicket(numbers='04 11 17 22 65',megaBall=7,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=True).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=True).save()
        GroupTicket(numbers='12 22 43 50 56',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=1),autoPick=True).save()

        GroupTicket(numbers='04 08 23 36 50',megaBall=5,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=False).save()
        GroupTicket(numbers='03 07 13 24 40',megaBall=3,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=False).save()
        GroupTicket(numbers='02 08 17 22 39',megaBall=4,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=False).save()
        GroupTicket(numbers='19 27 39 51 75',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=False).save()
        GroupTicket(numbers='04 11 17 22 65',megaBall=7,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=True).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=True).save()
        GroupTicket(numbers='12 22 43 50 56',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=2),autoPick=True).save()

        GroupTicket(numbers='04 08 23 36 50',megaBall=5,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=False).save()
        GroupTicket(numbers='03 07 13 24 40',megaBall=3,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=False).save()
        GroupTicket(numbers='02 08 17 22 39',megaBall=4,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=False).save()
        GroupTicket(numbers='19 27 39 51 75',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=False).save()
        GroupTicket(numbers='04 11 17 22 65',megaBall=7,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=True).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=True).save()
        GroupTicket(numbers='12 22 43 50 56',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=3),autoPick=True).save()

        GroupTicket(numbers='04 08 23 36 50',megaBall=5,agreementPeriod=AgreementPeriod.objects.get(pk=4),autoPick=False).save()
        GroupTicket(numbers='03 07 13 24 40',megaBall=3,agreementPeriod=AgreementPeriod.objects.get(pk=4),autoPick=False).save()
        GroupTicket(numbers='02 08 17 22 39',megaBall=4,agreementPeriod=AgreementPeriod.objects.get(pk=4),autoPick=False).save()
        GroupTicket(numbers='19 27 39 51 75',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=4),autoPick=False).save()
        GroupTicket(numbers='04 11 17 22 65',megaBall=7,agreementPeriod=AgreementPeriod.objects.get(pk=4),autoPick=True).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,agreementPeriod=AgreementPeriod.objects.get(pk=4),autoPick=True).save()

        GroupTicket(numbers='04 08 23 36 50',megaBall=5,agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=False).save()
        GroupTicket(numbers='03 07 13 24 40',megaBall=3,agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=False).save()
        GroupTicket(numbers='02 08 17 22 39',megaBall=4,agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=False).save()
        GroupTicket(numbers='19 27 39 51 70',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=False).save()
        GroupTicket(numbers='04 11 17 22 65',megaBall=7,agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=True).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=True).save()
        GroupTicket(numbers='04 15 23 45 62', megaBall=9, agreementPeriod=AgreementPeriod.objects.get(pk=5),autoPick=True).save()

        GroupTicket(numbers='03 07 13 24 40',megaBall=3,agreementPeriod=AgreementPeriod.objects.get(pk=6),autoPick=False).save()
        GroupTicket(numbers='04 08 23 36 50',megaBall=5,agreementPeriod=AgreementPeriod.objects.get(pk=6),autoPick=False).save()
        GroupTicket(numbers='04 15 23 45 62',megaBall=9,agreementPeriod=AgreementPeriod.objects.get(pk=6),autoPick=False).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,agreementPeriod=AgreementPeriod.objects.get(pk=6),autoPick=True).save()
        GroupTicket(numbers='19 27 39 51 70',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=6),autoPick=True).save()

        GroupTicket(numbers='02 22 17 04 28',megaBall=15,agreementPeriod=AgreementPeriod.objects.get(pk=7),autoPick=False).save()
        GroupTicket(numbers='63 70 66 15 44',megaBall=23,agreementPeriod=AgreementPeriod.objects.get(pk=7),autoPick=True).save()
        GroupTicket(numbers='38 69 36 63 16',megaBall=23,agreementPeriod=AgreementPeriod.objects.get(pk=7),autoPick=True).save()
        GroupTicket(numbers='50 25 11 24 39',megaBall=18,agreementPeriod=AgreementPeriod.objects.get(pk=7),autoPick=True).save()
        GroupTicket(numbers='09 62 29 10 35',megaBall=11,agreementPeriod=AgreementPeriod.objects.get(pk=7),autoPick=True).save()
        GroupTicket(numbers='64 25 34 66 44',megaBall=17,agreementPeriod=AgreementPeriod.objects.get(pk=7),autoPick=True).save()

        PaidOut(agreementPeriod=AgreementPeriod.objects.get(pk=1),prizeAmount="15").save()
        PaidOut(agreementPeriod=AgreementPeriod.objects.get(pk=2),prizeAmount="24").save()
        PaidOut(agreementPeriod=AgreementPeriod.objects.get(pk=3), prizeAmount="35").save()
        PaidOut(agreementPeriod=AgreementPeriod.objects.get(pk=4), prizeAmount="13").save()
        PaidOut(agreementPeriod=AgreementPeriod.objects.get(pk=5), prizeAmount="49").save()
        PaidOut(agreementPeriod=AgreementPeriod.objects.get(pk=6), prizeAmount="40").save()
