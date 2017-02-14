from django.core.management.base import BaseCommand, CommandError
import requests
import json
import datetime
from datetime import date
from results.models import Drawing, GroupTicket, PrizesWon
from results.services import checkprize

class Command(BaseCommand):
    help = 'Checks the internet for drawing results and check the group''s tickets'

    def handle(self, *args, **options):
        url = 'https://data.ny.gov/resource/h6w8-42p9.json'
        payload = {'$order':'draw_date DESC', '$limit': 3}
        r = requests.get(url=url,params=payload)
        data = json.loads(r.text)
        for result in data:
            drawdate = result['draw_date'].split('T')[0]
            if not Drawing.objects.filter(drawingDate=drawdate):
                a = Drawing(numbers=str(result['winning_numbers']),megaBall=int(result['mega_ball']),multiplier=result['multiplier'],drawingDate=drawdate)
                a.save()
                for ticket in GroupTicket.objects.all():
                    if ticket.agreementPeriod.startDate <=  (datetime.datetime.strptime(drawdate, '%Y-%m-%d').date()) <= ticket.agreementPeriod.endDate:
                        checkprize(drawingid=a.id,ticketid=ticket.id)