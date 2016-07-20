from django.contrib import admin

from .models import Drawing
from .models import GroupTicket
from .models import PrizesWon
from .models import GroupPlayers
from .models import MegaNumbers


admin.site.register(MegaNumbers)
admin.site.register(Drawing)
admin.site.register(GroupTicket)
admin.site.register(PrizesWon)
admin.site.register(GroupPlayers)
