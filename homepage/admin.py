from django.contrib import admin
from .models import Homepost
@admin.register(Homepost)
class HomepostAdmin(admin.ModelAdmin):
    pass
