from results.models import Drawing, PrizesWon, GroupTicket
import datetime

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

def calcprizeAfterNovember2017(numnumbers, megaball):
    if numnumbers==5 and megaball:
        return 15000000
    if numnumbers==5 and not megaball:
        return 1000000
    if numnumbers==4 and megaball:
        return 10000
    if numnumbers==4 and not megaball:
        return 500
    if numnumbers==3 and megaball:
        return 200
    if numnumbers==3 and not megaball:
        return 10
    if numnumbers==2 and megaball:
        return 10
    if numnumbers==1 and megaball:
        return 4
    if numnumbers==0 and megaball:
        return 2
    else:
        return None

def checkprize(drawingid,ticketid):
    a = Drawing.objects.get(pk=drawingid)
    b = GroupTicket.objects.get(pk=ticketid)
    nummatch = 0
    megamatch = False
    for val in b.numbers_as_list():
        if val in a.numbers_as_list():
            nummatch = nummatch + 1
    if b.megaBall==a.megaBall:
        megamatch=True
    if a.drawingDate > datetime.date(2017, 10, 31):
        prizeamount = calcprizeAfterNovember2017(numnumbers=nummatch, megaball=megamatch)
    else:
        prizeamount = calcprize(numnumbers=nummatch, megaball=megamatch)
    if prizeamount:
        c = PrizesWon(drawing=a,ticket=b,groupPrizeAmount=prizeamount)
        c.save()
        print (c)