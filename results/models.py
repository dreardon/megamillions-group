from django.db import models


class MegaNumbers(models.Model):
    numbers = models.CharField(max_length=14, default=0)
    megaBall = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Mega Numbers"

    def __unicode__( self ):
        return "{0} {1}".format(self.numbers, "Megaball "+str(self.megaBall))

class Drawing(models.Model):
    megaNumbers = models.ForeignKey(MegaNumbers)
    multiplier = models.IntegerField()
    drawingDate = models.DateField()

    def __unicode__( self ):
        return "{0}".format(self.drawingDate)


class GroupTicket(models.Model):
    megaNumbers = models.ForeignKey(MegaNumbers)

    class Meta:
        verbose_name_plural = "Group Tickets"

    def __unicode__( self ):
        return "{0}".format(self.megaNumbers)


class PrizesWon(models.Model):
    drawing = models.ForeignKey(Drawing)
    groupPrizeAmount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Prizes Won"

    def __unicode__( self ):
        return "{0} {1}".format(self.drawing, self.groupPrizeAmount)

class GroupPlayers(models.Model):
    initials = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Group Players"

    def __unicode__( self ):
        return "{0}".format(self.initials)