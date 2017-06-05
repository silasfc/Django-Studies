from django.contrib import admin

from .models import Band, Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'instrument')
    list_filter = ('band',)


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass
