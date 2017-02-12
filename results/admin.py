from django.contrib import admin

from .models import Drawing
from .models import GroupTicket
from .models import AgreementPeriod
from .models import PaidOut
from .models import PrizesWon

admin.site.register(Drawing)
admin.site.register(GroupTicket)
admin.site.register(AgreementPeriod)
admin.site.register(PaidOut)
admin.site.register(PrizesWon)
