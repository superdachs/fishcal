from django.contrib import admin
from cal.models import Bundesland
from cal.models import Mindestmass
from cal.models import Schonzeit

admin.site.register(Bundesland)
admin.site.register(Mindestmass)
admin.site.register(Schonzeit)


