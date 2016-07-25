from django.core.management.base import BaseCommand, CommandError
import requests
import json
from results.models import Drawing, GroupTicket, PrizesWon
from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Command(BaseCommand):
    help = 'Checks the internet for drawing results and check the group''s tickets'

    def handle(self, *args, **options):
        url = 'https://data.ny.gov/resource/h6w8-42p9.json'
        payload = {'$order':'draw_date DESC', '$limit': 26}
        r = requests.get(url=url,params=payload)
        data = json.loads(r.text)
        in_dates = Drawing.objects.values_list('drawingDate')
        for result in data:
            drawdate = result['draw_date'].split('T')[0]
            if not Drawing.objects.filter(drawingDate=drawdate):
                a = Drawing(numbers=str(result['winning_numbers']),megaBall=int(result['mega_ball']),multiplier=result['multiplier'],drawingDate=drawdate)
                a.save()
                winningnumbers = str(result['winning_numbers']).split()
                winningmegaball = int(result['mega_ball'])
                for ticket in GroupTicket.objects.all():
                    numMatch = 0
                    megaMatch = False
                    ticket_megaball = ticket.megaBall
                    ticket_numbers = ticket.numbers
                    for val in ticket_numbers:
                        if val in winningnumbers:
                            numMatch = numMatch + 1
                    if ticket_megaball==winningmegaball:
                        megaMatch=True
                    prizeAmount = self.calcprize(numnumbers=numMatch, megaball=megaMatch)
                    if prizeAmount:
                        b = PrizesWon(drawing=a,ticket=ticket,groupPrizeAmount=prizeAmount)
                        b.save()
                        print b


    @staticmethod
    def calcprize(numnumbers, megaball):
        if numnumbers==5 and megaball:
            return 15000000
        if numnumbers==5 and not megaball:
            return 1000000
        if numnumbers==4 and megaball:
            return 5000
        if numnumbers==4 and not megaball:
            return 500
        if numnumbers==3 and megaball:
            return 50
        if numnumbers==3 and not megaball:
            return 5
        if numnumbers==2 and megaball:
            return 5
        if numnumbers==1 and megaball:
            return 2
        if numnumbers==0 and megaball:
            return 1
        else:
            return None