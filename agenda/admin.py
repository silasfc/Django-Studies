from django.contrib import admin
from agenda.models import Person, Telephone, Email, Register


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name')


class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('number', 'kind')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('address', 'kind')


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'father', 'mother', 'birth_date', 'address', 'personal_email', 'institutional_email', 'phone', 'cell_phone')


admin.site.register(Person)
admin.site.register(Telephone, TelephoneAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Register, RegisterAdmin)
