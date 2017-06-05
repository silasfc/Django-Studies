from django.contrib import admin

from .models import NaturalPerson, Involved, Incident, Victim, Offender


admin.site.register(NaturalPerson)
# admin.site.register(Involved)
admin.site.register(Incident)
admin.site.register(Victim)
admin.site.register(Offender)
