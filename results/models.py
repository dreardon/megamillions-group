from django.db import models


class AgreementPeriod(models.Model):
    periodName = models.CharField(max_length=14, default=0)
    agreementFile = models.FileField(upload_to='attachments',null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Agreement Periods"

    def __str__( self ):
        return "{0} {1} {2} {3}".format(self.periodName, self.startDate, '-', self.endDate)

    def getRange(self):
        return "{0} {1} {2}".format(self.startDate, '-', self.endDate)

    def getName(self):
        return "{0}".format(self.periodName)


class MegaNumbers(models.Model):
    numbers = models.CharField(max_length=14, default=0)
    megaBall = models.IntegerField(default=0)

    def numbers_as_list(self):
        return self.numbers.split(' ')


class Drawing(MegaNumbers):
    multiplier = models.IntegerField()
    drawingDate = models.DateField()

    def __str__( self ):
        return "{0} {1} {2}".format(self.drawingDate, 'Numbers: ' + self.numbers, 'Megaball: ' + str(self.megaBall))


class GroupTicket(MegaNumbers):
    autoPick = models.BooleanField()
    agreementPeriod = models.ForeignKey(AgreementPeriod,null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Group Tickets"

    def __str__( self ):
        return "{0} {1} {2} {3}".format('Numbers: '+self.numbers, 'Megaball: '+str(self.megaBall),'AutoPick: '+str(self.autoPick), 'Agreement Period:' +str(self.agreementPeriod))


class PrizesWon(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    ticket = models.ForeignKey(GroupTicket, on_delete=models.CASCADE)
    groupPrizeAmount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Prizes Won"

    def __str__( self ):
        return "{0} {1} {2}".format(self.drawing, self.ticket, self.groupPrizeAmount)


class PaidOut(models.Model):
    agreementPeriod = models.ForeignKey(AgreementPeriod, on_delete=models.CASCADE)
    prizeAmount = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Paid Out"

    def __str__( self ):
        return "{0} {1}".format(self.agreementPeriod, self.prizeAmount)