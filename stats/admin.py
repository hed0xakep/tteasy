from django.contrib import admin
from .models import PrivateStatisticsModel, PublicStatisticsModel

@admin.register(PrivateStatisticsModel)
class PrivateStatisticsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PublicStatisticsModel)
class PublicStatisticsModelAdmin(admin.ModelAdmin):
    pass
