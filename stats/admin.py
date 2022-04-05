from django.contrib import admin
from .models import PrivateStatisticsModel, PublicStatisticsModel

admin.site.register(PrivateStatisticsModel)
admin.site.register(PublicStatisticsModel)
