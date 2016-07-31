from django.db import models


class MegaNumbers(models.Model):
    numbers = models.CharField(max_length=14, default=0)
    megaBall = models.IntegerField(default=0)

    def numbers_as_list(self):
        return self.numbers.split(' ')


class Drawing(MegaNumbers):
    multiplier = models.IntegerField()
    drawingDate = models.DateField()

    def __unicode__( self ):
        return "{0} {1} {2}".format(self.drawingDate, 'Numbers: ' + self.numbers, 'Megaball: ' + str(self.megaBall))


class GroupTicket(MegaNumbers):
    active = models.BooleanField()
    autoPick = models.BooleanField()

    class Meta:
        verbose_name_plural = "Group Tickets"

    def __unicode__( self ):
        return "{0} {1} {2} {3}".format('Numbers: '+self.numbers, 'Megaball: '+str(self.megaBall),'AutoPick: '+str(self.autoPick),'Active: '+str(self.active))


class PrizesWon(models.Model):
    drawing = models.ForeignKey(Drawing)
    ticket = models.ForeignKey(GroupTicket)
    groupPrizeAmount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Prizes Won"

    def __unicode__( self ):
        return "{0} {1} {2}".format(self.drawing, self.ticket, self.groupPrizeAmount)
