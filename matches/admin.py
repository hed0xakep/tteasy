from django.contrib import admin
from .models import MatchModel
@admin.register(MatchModel)
class MatchModelAdmin(admin.ModelAdmin):
    pass
