from django.contrib import admin
from agenda.models import Person, Telephone, Email, Register


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    pass

# or...
# admin.site.register(Person)
# admin.site.register(Telephone)
# admin.site.register(Email)
# admin.site.register(Register)
