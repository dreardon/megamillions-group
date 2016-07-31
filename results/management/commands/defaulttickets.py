from django.core.management.base import BaseCommand, CommandError
import requests
import json
from results.models import GroupTicket
from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Command(BaseCommand):
    help = 'Creates the set of default tickets'

    def handle(self, *args, **options):
        GroupTicket(numbers='04 08 23 36 50',megaBall=5,active=True,autoPick=False).save()
        GroupTicket(numbers='03 07 13 24 40',megaBall=3,active=True,autoPick=False).save()
        GroupTicket(numbers='02 08 17 22 39',megaBall=4,active=True,autoPick=False).save()
        GroupTicket(numbers='19 27 39 51 75',megaBall=15,active=True,autoPick=False).save()
        GroupTicket(numbers='04 11 17 22 65',megaBall=7,active=True,autoPick=True).save()
        GroupTicket(numbers='05 15 20 34 55',megaBall=14,active=True,autoPick=True).save()
        GroupTicket(numbers='12 22 43 50 56',megaBall=15,active=True,autoPick=True).save()
